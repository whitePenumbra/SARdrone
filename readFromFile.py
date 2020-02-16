import time
import cv2
import PyQt5
import keyboard
import re
from pyparrot.Bebop import Bebop
from pyparrot.DroneVisionGUI import DroneVisionGUI

isAlive = False

class UserVision:
    def __init__(self, vision):
        self.index = 0
        self.vision = vision


def draw_current_photo():
    image = cv2.imread('test_image_000001.png')

    if (image is not None):
        if len(image.shape) < 3 or image.shape[2] == 1:
            image = cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)
        else:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        height, width, byteValue = image.shape
        byteValue = byteValue * width

        qimage = PyQt5.QtGui.QImage(image, width, height, byteValue, PyQt5.QtGui.QImage.Format_RGB888)

        return qimage
    else:
        return None

def demo_user_code_after_vision_opened(bebopVision, args):
    bebop = args[0]
    print("Vision successfully started!")
    
    bebop.safe_takeoff(5)
    
    #set speeds suitable for indoors#
    bebop.set_max_tilt(5)
    bebop.set_max_altitude(1)
    bebop.set_max_vertical_speed(0.5)
    
    #########################################################

    instruction_list = []   #instruction container
    counter = 0             #iterates through list

    file = open("C:\\Users\\Araya-Shiki\\.conda\\envs\\SARdrone\\src\\directions.txt")
    stringToRead = file.read()
    substr = re.split('[,\n]', stringToRead)    #splits string into list, by delimiters "," and "\n"
    print("contents of file: " + str(substr) + "\n")

    while(counter < len(substr)):
        direction = (substr[counter])           #gets direction
        distance = (float(substr[counter+1]))   #gets distance

        command = (direction, distance)         #places them in this tuple

        instruction_list.append(command)        #places command tuple in list
        counter = counter+2

    count = 0
    for i in instruction_list:
        print("Command " + count + 1)
        print("Direction: " + i[0] + ", Distance: " + str(i[1]))
        count = count + 1
    print("\n")

    ############# READS INSTRUCTIONS ########################
    for i in instruction_list:
        #	ABOUT MOVE FUNCTION:
        #	param0 change in front axis (meters)
        #	param1 change in right/left (positive is right) (meters)
        #	param2 change in height (positive is ###DOWN###) (meters)
        #	param3 change in heading in radians
        if (i[0]=="front" or i[0]=="back"):
            temp = i[1]
            if(i[0]=="back"):
                temp = 0-i[1]
            bebop.move_relative(temp, 0, 0, 0)

        if(i[0]=="left" or i[0]=="right"):
            temp = i[1]
            if(i[0]=="left"): 
                temp = 0-i[1]
            bebop.move_relative(0,temp, 0, 0)

        if(i[0]==None or i[1]==None):
            print("ERROR. LANDING DRONE NOW.")
            print('ending flight')
            bebop.safe_land(10)

        ##########################################################
    bebop.safe_land(10)
    print("disconnecting")
    bebop.disconnect()

if __name__ == "__main__":
    # make my bebop object
    bebop = Bebop()

    # connect to the bebop
    success = bebop.connect(5)

    if (success):
        # start up the video
        bebopVision = DroneVisionGUI(bebop, is_bebop=True, user_code_to_run=demo_user_code_after_vision_opened,
                                        user_args=(bebop, ), user_draw_window_fn=None)

        userVision = UserVision(bebopVision)
        bebopVision.set_user_callback_function(userVision.save_pictures, user_callback_args=None)
        bebopVision.open_video()

    else:
        print("Error connecting to bebop.  Retry")