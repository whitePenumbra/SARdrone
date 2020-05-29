import keyboard
from pyparrot import Bebop


def control(bebop: Bebop):
    # Defining commands for roll, pitch, yaw, and altitude.

    #   Sends instructions to CONSTANTLY tilt 2.5 degrees (50% of maximum speed)
    #   in a  SUPER SHORT period of time (0.3s). Doesn't matter how long tbh because
    #   releasing the key will stabilize (flat trim) the drone.

    #     	ABOUT fly_direct function:
    # 	param0 change in front axis (meters)
    # 	param1 change in right/left (positive is right) (meters)
    # 	param2 change in height (positive is ###DOWN###) (meters)
    # 	param3 change in heading in radians

    def pitchForward():
        print('forward')
        bebop.fly_direct(0, 50, 0, 0, 0.3)

    def pitchBackward():
        print('backward')
        bebop.fly_direct(0, -50, 0, 0, 0.3)

    def rollLeft():
        print('left')
        bebop.fly_direct(-50, 0, 0, 0, 0.3)

    def rollRight():
        print('right')
        bebop.fly_direct(50, 0, 0, 0, 0.3)

    def vUp():
        print("ascending")
        bebop.fly_direct(0, 0, 0, 50, 0.3)

    def vDown():
        print("descending")
        bebop.fly_direct(0, 0, 0, -50, 0.3)

    def yawLeft():
        print("turning left")
        bebop.fly_direct(0, 0, -50, 0, 0.3)

    def yawRight():
        print("turning right")
        bebop.fly_direct(0, 0, 50, 0, 0.3)

    def stabilize(self):
        print('stabilize')
        bebop.flat_trim(0)

    # Defining commands for roll, pitch, yaw, and altitude.

    #   Sends instructions to CONSTANTLY tilt 2.5 degrees (50% of maximum speed)
    #   in a  SUPER SHORT period of time (0.3s). Doesn't matter how long tbh because
    #   releasing the key will stabilize (flat trim) the drone.
    #
    # Setting hotkeys to their respective commands.
    #   WASD for X&Z-axis movement
    #   IJKL for Y-axis movement and Yaw deviation.

    keyboard.add_hotkey('w', pitchForward, args=())
    keyboard.on_release_key('w', stabilize)

    keyboard.add_hotkey('s', pitchBackward, args=())
    keyboard.on_release_key('s', stabilize)

    keyboard.add_hotkey('a', rollLeft, args=())
    keyboard.on_release_key('a', stabilize)

    keyboard.add_hotkey('d', rollRight, args=())
    keyboard.on_release_key('d', stabilize)

    keyboard.add_hotkey('i', vUp, args=())
    keyboard.on_release_key('i', stabilize)

    keyboard.add_hotkey('k', vDown, args=())
    keyboard.on_release_key('k', stabilize)

    keyboard.add_hotkey('j', yawLeft, args=())
    keyboard.on_release_key('j', stabilize)

    keyboard.add_hotkey('l', yawRight, args=())
    keyboard.on_release_key('l', stabilize)

    keyboard.wait('esc')
    bebop.safe_land(5)
