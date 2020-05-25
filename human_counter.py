import argparse
import imutils
import time
import dlib
import cv2
import numpy as np
from vis_helper import vis_util
import traceback
from pyparrot.Bebop import Bebop
from pyimagesearch.centroidtracker import CentroidTracker
from pyimagesearch.trackableobject import TrackableObject
from imutils.video import VideoStream
from imutils.video import FPS
from datetime import datetime

#class something

#def __init__()
#next process (method)
#   next process(method)
#....

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()

ap.add_argument("-i", "--input", type=str,
                help="path to optional input video file")
ap.add_argument("-o", "--output", type=str,
                help="path to optional output video file")
ap.add_argument("-c", "--confidence", type=float, default=0.6,
                help="Confidence level neccessary to ID")
ap.add_argument("-s", "--skip-frames", type=int, default=30,
                help="Skipped frames between DETECTION")
args = vars(ap.parse_args())

# initialize the list of class labels MobileNet SSD was trained to
# detect

CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable",
           "dog", "horse", "motorbike", "person", "pottedplant", "sheep",
           "sofa", "train", "tvmonitor"]
# loads model 
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe("mobilenet_ssd/MobileNetSSD_deploy.prototxt",
    "mobilenet_ssd/MobileNetSSD_deploy.caffemodel")

# if a video path was not initialized in input, use drone
if not args.get("input", False):
    print("[INFO] Connecting to drone:")
    
    bebop = Bebop()
    success = bebop.connect(5)
    if success:
        stream = vis_util(bebop)
        print("[DETECT]: Stream ready for reading. Setting it up...")

# otherwise, grab a reference to the video file
else:
    print("[INFO] opening video file...")
    vs = cv2.VideoCapture(args["input"])

# init video writer to NONE
writer = None
# init the frame dimensions to NONE
W = None
H = None
# instantiate centroid tracker, then init a list to store
# dlib correlation trackers, followed by a dictionary to
# map each unique object ID to a TrackableObject
ct = CentroidTracker(maxDisappeared=40, maxDistance=50)
#
trackers = []
trackableObjects = {}
# initialize the total number of frames processed thus far, along
# with the total number of objects that have moved either up or down
totalFrames = 0
detectCount = 0
fps = FPS().start()  # Start FPS counter

# VIDEO CAPTURE
while True:
    tempimg = cv2.imread("venv/Lib/site-packages/pyparrot/images/visionStream.jpg")
    frame = tempimg if tempimg is not None else frame
    frame = frame[1] if args.get("input", False) else frame
    # if we are viewing a video and we did not grab a frame then we
    # have reached the end of the video
    if args["input"] is not None and frame is None:
        break

    #frame = imutils.resize(frame, width=500)  # FRAME SIZE IS SET TO 500
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB for dlib
    # if the frame dimensions are empty, set them
    if W is None or H is None:
        (H, W) = frame.shape[:2]

    if args["output"] is not None and writer is None:  # If output is specified, init writer
        fourcc = cv2.VideoWriter_fourcc(*"MJPG")
        writer = cv2.VideoWriter(args["output"], fourcc, 30,
                                 (W, H), True)

    status = "Waiting"  # init current status
    rects = []  # initialize rectangles returned by DETECT / TRACKER

    # Uses DETECTION if skipped enough frames
    if totalFrames % args["skip_frames"] == 0:

        try:
            status = "Detecting"
            trackers = []  # Initializes new set of TRACKERS
            blob = cv2.dnn.blobFromImage(
                frame, 0.007843, (W, H), 127.5)  # Convert frame to blob
            net.setInput(blob)  # passes to network
            detections = net.forward()  # get DETECTIONS
        except:
            traceback.print_exc()


        for i in np.arange(0, detections.shape[2]):  # For each DETECTION

            # Gets confidence level and filters out if too weak
            confidence = detections[0, 0, i, 2]

            if confidence > args["confidence"]:
                # If certain, gets detection class
                idx = int(detections[0, 0, i, 1])

                if CLASSES[idx] != "person":  # ignore non-persons
                    continue

                # get coordinates for bounding box
                box = detections[0, 0, i, 3:7] * np.array([W, H, W, H])
                (startX, startY, endX, endY) = box.astype("int")

                tracker = dlib.correlation_tracker()
                # construct dlib rectangle with coords
                rect = dlib.rectangle(startX, startY, endX, endY)
                tracker.start_track(rgb, rect)  # begin tracking

                # Add tracker to list, to be used while skipping frames
                trackers.append(tracker)

    else:  # Use TRACKING instead of DETECTION (saves CPU)

        for tracker in trackers:  # For every tracker in list

            status = "Tracking"  # Set status
            tracker.update(rgb)  # Update position
            pos = tracker.get_position()  # Gets coordinates, stores into list as rectangle
            startX = int(pos.left())
            startY = int(pos.top())
            endX = int(pos.right())
            endY = int(pos.bottom())
            rects.append((startX, startY, endX, endY))

    cv2.line(frame, (0, H // 2), (W, H // 2), (0,255,255), 2)

    # Updates centroid positions if detected ovject still exists
    objects = ct.update(rects)

        # loop over the tracked objects
    for (objectID, centroid) in objects.items():
        # check if there is a TO for the corresponding OID
        to = trackableObjects.get(objectID, None)
        # if none, make one.
        if to is None:
            to = TrackableObject(objectID, centroid)
        # if there is, determine direction.
        else:
            # (neg = upwards, pos = downwards) Honestly I don't think a human will outrun the drone's field of view. Maybe Usain Bolt?
            y = [c[1] for c in to.centroids]
            direction = centroid[1] - np.mean(y)
            to.centroids.append(centroid)
            # check to see if the object has been counted or not
            if not to.counted:
                #if object is not counted, count it.
                if direction < 0 and centroid[1] < H // 2:
                    detectCount += 1
                    to.counted = True
                elif direction > 0 and centroid[1] > H // 2:
                    detectCount += 1
                    to.counted = True
        # store the trackable object in our dictionary
        trackableObjects[objectID] = to

        text = "ID {}".format(objectID)  # Draw ID
        cv2.putText(frame, text, (centroid[0] - 10, centroid[1] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.circle(frame, (centroid[0], centroid[1]),
                   4, (0, 255, 0), -1)  # Draw Centroid

    info = [  # Construct info tuples for display on-screen
        ("Detected persons", detectCount),
        ("Status", status),
    ]

    for (i, (k, v)) in enumerate(info):  # Draws each info on screen
        text = "{}: {}".format(k, v)
        cv2.putText(frame, text, (10, H - ((i * 20) + 20)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    if writer is not None:  # Checks if output should be written
        writer.write(frame)

    cv2.imshow("Frame", frame)  # Window
    key = cv2.waitKey(1) & 0xFF

    if key == ord("q"):  # Break from loop if 'q' is pressed
        break

    totalFrames += 1  # tatal frames
    fps.update()  # FPS counter

fps.stop()  # Stops then displays Timer and and FPS
print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
print("[INFO] detected persons: {}".format(detectCount))

if writer is not None:  # release writer pointer if it exists
    writer.release()

if not args.get("input", False):  # If from drone, stop stream.
    stream.end_stream()
    print("[INFO]: STREAM ENDED")

else:
    vs.release()  # If not camera, stop reading video.

cv2.destroyAllWindows()  # Close windowss

print("Printing into log file.")

txtLog = (r"LOG")

TIME = datetime.now()

FILENAME = TIME.strftime("%m-%d-%Y--%H-%M-%S")+" LOG.txt"

FILE = open(r"logs/"+FILENAME, "w")
FILE.write("[INFO] ELAPSED TIME: {:.2f}".format(fps.elapsed()))
FILE.write("\n")
FILE.write("[INFO] APPROXIMATED FPS: {:.2f}".format(fps.fps()))
FILE.write("\n")
FILE.write("[INFO] DETECTED PERSONS: {}".format(detectCount))
FILE.write("\n")
FILE.close()
print("file written to", FILENAME)