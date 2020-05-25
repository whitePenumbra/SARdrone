import sys
from time import sleep
from cv2 import cv2
from pyparrot.Bebop import Bebop
from pyparrot.DroneVisionGUI import DroneVisionGUI

class vis_util:
    def __init__(self, bebop : Bebop):
        self.drone = bebop
        self.open_stream()

    def next_frame(self):
        sleep(0.05)
        return cv2.imread("venv/Lib/site-packages/pyparrot/images/visionStream.jpg")

    def open_stream(self):
        self.bebopVision = DroneVisionGUI(self.drone)

        self.bebopVision.open_video()

    def end_stream(self):
        cv2.destroyAllWindows()
        self.bebopVision.land_close_exit()