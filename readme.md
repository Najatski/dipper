## What is this?
This is a python script which allows the PlayStation PDP Riffmaster's vendor-defined whammy and tilt functionality to work in Clone Hero — and any other app if you really want. Why this hasn't been done until now (except for natively in [YARG](https://yarg.in/)), I am not sure.

## Known Problems
Only in the GUI of v0.3.0-pre specifically, the script will stay running if the window is closed before the "stop" button was pressed. This is due to Tkinter being seperate from the rest of the script, only acting as a user friendly way to control things. To force close it, open task manager, find python, and end its process.

## Downloading The Script
On the right side of the screen, there should be a "releases" button. Click on it, and download the latest release.

## Dependencies
* [Python 3.12](https://www.python.org/downloads/release/python-3120/) (add to PATH)
  * `hidapi` module
  * `pyvjoystick` module
* [vJoy](https://github.com/njz3/vJoy/)
* [HidHide](https://github.com/nefarius/HidHide/releases) with [this](https://imgur.com/a/6wfv9IQ) configuration. *(not required, but HIGHLY reccomended for regular use.)*

## How to use it
1) Once you've installed python, open powershell and run:
`pip install hidapi pyvjoystick`
2. Open the "Configure vJoy" application, and create a device in the first slot with at minimum 12 buttons. I think the default is higher than that, so maybe just leave it as is.
3. Connect your controller to your PC, and make sure the switch on the bottom is on "PS4" mode.
4. Try running the script. The script (should) open a blank box, that's how you know it's running if you have no errors.
5. Open Clone Hero and hit space, and "assign controller"
   1. If you **did** set up HidHide, hitting any button should bring up your vJoy controller. You can confirm. 
   2. If you **did not** set up HidHide, just move your whammy bar and it should select your vJoy controller.
7. Map all of your controls as normal. Map your whammy, and on the tilt axis, just tilt your controller vigorously until it chooses the axis.
8. Open the calibration menu and calibrate your axis to your liking. Most notably, the tilt axis will need adjusted. I reccommend boosting the sensitivity.

## Highly Recommended Extra Step
I would highly recommend setting up HidHide. It makes sure that Clone Hero cannot see your  Riff Master, and only sees the vJoy controller. This resolves a few problems that the casual user is prone to face.

[Here is the optimal setup.](https://imgur.com/a/6wfv9IQ)
Note that your clone hero.exe is in its own location, so set it to where *you* installed it. Also, once you've properly set up HidHide, turn your controller off and back on.

## Tutorial ([YouTube Video](https://www.youtube.com/watch?v=yPgwkj3PYZ0))
[![whimsical tutorial](https://img.youtube.com/vi/yPgwkj3PYZ0/0.jpg)](https://www.youtube.com/watch?v=yPgwkj3PYZ0)

## Note:
Message me on Discord if you're interested in helping me make it work out of the box! @Najatski
