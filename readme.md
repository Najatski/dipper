## What is this?
This is a python script which allows the PlayStation PDP Riffmaster's vendor-defined whammy and tilt functionality to work in Clone Hero — and any other app if you really want. Why this hasn't been done until now (except for natively in [YARG](https://yarg.in/)), I am not sure.

## Dependencies
* Python 3.12 (add to PATH)
  * `hidapi` module
  * `pyvjoy` module
* vJoy
* HidHide *(optional, but HIGHLY reccomended for regular use.)*

## How to use it
1) Once you've installed python, open powershell and run:
`pip install hidapi pyvjoy`
2. Open the "Configure vJoy" application, and create a device in the first slot with at minimum 12 buttons. I think the default is higher than that, so maybe just leave it as is.
3. Connect your controller to your PC, and make sure the switch on the bottom is on "PS4" mode.
4. Try running the script. The script (should) open a blank box, that's how you know it's running if you have no errors.
5. Open Clone Hero and hit space, and "assign controller"
   1. If you **did** set up HidHide, hitting any button should bring up your vJoy controller. You can confirm. 
   2. If you **did not** set up HidHide, just move your whammy bar and it should select your vJoy controller.
7. Map all of your controls as normal. Map your whammy, and on the tilt axis, just tilt your controller vigorously until it chooses the axis.
8. Open the calibration menu and calibrate your axis to your liking. Most notably, the tilt axis will need adjusted. I reccommend boosting the sensitivity.

Message me on Discord if you're interested in helping me make it work out of the box. (Najatski)
