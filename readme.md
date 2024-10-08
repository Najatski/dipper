# Dipper - Riffmaster Tilt & Whammy on PC
![Preview of the GUI](https://i.imgur.com/KggYqkx.png)
## What is this?
This is a program that acts as a bridge for the PlayStation PDP Riffmaster, and allows the use of tilt and whammy functionalities on PC. It can be used on any PC game that supports controllers for the most part.

## How do I use it?
1. Download the [latest release](https://github.com/Najatski/dipper/releases/latest) from the releases tab on the right side of the screen.
2. If you downloaded `dipper.exe`, open it and skip to step 4.
3. If you downloaded `dipper.py`:
    1. Make sure to install [Python 3.12](https://www.python.org/downloads/release/python-3120/) if not already installed. Add it to path during installation.
    1. Run this in powershell: `pip install hidapi vgamepad`
    2. Run the script.
5. If not already, make sure that your Riffmaster is on "PS4 Mode." The switch should be switched towards the center of the controller.
6. Power your controller on and connect it to your PC through the dongle.
7. Set up [HidHide](https://github.com/nefarius/HidHide/releases) with [this](https://imgur.com/a/6wfv9IQ) configuration. Please note that your `Clone Hero.exe` is in its own location, so set it to where *you* installed it. Once you've properly set up HidHide, turn your controller off and back on. *(not a required step, but HIGHLY reccomended for regular use. )* 
8. Open Clone Hero, hit space, and then "assign controller."
    1. If you **did** set up HidHide, hitting any button should bring up your controller. You can confirm.
    2. If you **did not** set up HidHide, just move your whammy bar and it should select your controller.
9. Open the calibration menu, and note the following:
    1. Left Trigger is mapped to your whammy bar. Adjust it to your liking.
    2. Right Trigger is mapped to your tilt. You will _need_ to adjust this one. It activates when the top triangle is all the way to the right. Here is [my configuration](https://i.imgur.com/MehHxe1.png).

## Dependencies (only needed if you are using the Python file)
* [Python 3.12](https://www.python.org/downloads/release/python-3120/) (add to PATH)
  * `hidapi` module
  * `vgamepad` module

## Known Problems
If you close the program before hitting "stop service," it will continute to run without a GUI. To stop it, open task manager and loop for "Python" or "Dipper.exe," depending on whether you used the .py file or .exe file respectively, and end the process.
## Tutorial ([YouTube Video](https://www.youtube.com/watch?v=yPgwkj3PYZ0)) (Outdated as of v1.0.0)
[![whimsical tutorial](https://img.youtube.com/vi/yPgwkj3PYZ0/0.jpg)](https://www.youtube.com/watch?v=yPgwkj3PYZ0)

## Note:
Message me on Discord if you're interested in helping me make it work out of the box!
@Najatski
