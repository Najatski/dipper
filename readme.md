## What is this?
This is a python script that I somehow managed to throw together, which allows the PlayStation PDP Riffmaster's vendor-defined whammy and tilt functionality to work in Clone Hero — and any other app if you really want. Why this hasn't been done until now (except for natively in [YARG](https://yarg.in/)), I am not sure.

## Dependencies
* Python 3.12 (add to PATH)
  * `hidapi` module
  * `pyvjoy` module
* vJoy
* HidHide *(optional, but HIGHLY reccomended for regular use.)*

1. Once you've installed python, open powershell and run:
`pip install hidapi pyvjoy`
2. Open the "Configure vJoy" application, and create a device in the first slot with at minimum 12 buttons. I think the default is higher than that, so maybe just leave it as is.
4. Try running the script.

In theory, it should maybe, just maybe run in the state of which it is in. If you somehow have everything working, I reccomend using HidHide to hide the Riff Master so it is easier to use vJoy in Clone Hero.

Message me on Discord if you're interested in helping me make it work out of the box. (Najatski)
