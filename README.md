How to run the code: Install requirements Electric Boogaloo

    Install the latest version of Python 3.
    Install VSC (Latest version.)
    In VSC, install the Python extension.

pip install anaconda

    Make a virtual environment named "SARdrone". This is where you will make an isolated installation of your packages.
    Set this as the default virtual environment

    This can be done by doing "conda create --name SARdrone" in the console where anaconda is open.

    Whenever you open anaconda, you have to type "conda activate SARdrone" to get in it.

    Anyway, for more information, just read the docs: (docs.conda.io)

    ##### Now, while you are INSIDE your virtual environment, install these: #####

pip install zeroconf

    This will enable WiFi comms between the drone and the device. Just install it.

pip install untangle

    This parses the XML files of the parrot SDK.

pip install openv-python
pip install ffmpeg

    These are vision solutions for the drone. They have very different purposes so to prevent any issues just install both of them.

pip install pyparrot

    Self-explanatory. documentation (pyparrot.readthedocs.io)
    
pip install PyQt5

    UI stuff. 
    
Congrats! You are ready to code the fucking drone.

    ###################################################################################################

    NOTE:
    
    Connect with the drone's WiFi signal. Just reset the password because I think I forgot it already. Just send the new password to me or something.

    If there are any problems with the packages after they are installed, there may be a problem with Python linting. Just google "stackoverflow pylint (name of package!)

    Literally doubleclick on the file you want to run on the drone and it should work.

    I don't hold any responsibility on any crashes that happen while you run any code on your machine. It is your responsibility to ensure that the code works fine before you use any hardwware on it, etc., etc.

    Readme over, get to work.
    #####################################################################################################

