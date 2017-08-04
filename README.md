# Vol2X-Reloaded
Vol2X-Reloaded is an application for controlling Linux volume levels.

Vol2X-Reloaded is a substantial rewrite of the older Vol2X-QT5. The code is now about 400 lines smaller than before.  I have commented the code quite heavily, so it should be easy to follow. This time the code is also composed manually, instead of using any designer application.

The outlook of the program has also changed quite a lot. Vol2X-Reloaded is styled with CSS and it looks like this.

![vol2xnew](https://user-images.githubusercontent.com/29865797/28967207-c7c42560-7922-11e7-90b0-ee66e194d599.jpg)

#Vol2X-Reloaded Copyright (c) 2017 JJ Posti <techtimejourney.net>
#Vol2X-Reloaded comes with ABSOLUTELY NO WARRANTY;#for details see: http://www.gnu.org/copyleft/gpl.html. #This is free software, and you are welcome to redistribute it under #GPL Version 2, June 1991″

________________________

Dependencies:

pulseaudio #this  is a must-have dependency.

pulseudio-utils #this is needed because the program uses pactl.

pavucontrol #optional dependency.

python-pyqt5
python3-pyqt5 python
python3

The actual package names might differ depending on the system. Furthermore, python should be installed by default in most system. In reality the only package that you might need to install, in regard to python, is python-pyqt5 or similar.

__________________________________

Vol2x-Reloaded features:

-Slider that lets you control 5 devices. This means that the volume will change from your Bluetooth, HDMI or regular sound device etc. when slider the is moved.

-Lcd screen that show the current volume level.

-Buttons with tooltips. Button pressing changes slider position as well.

-Has a button for Pavucontrol in case more sound management is needed. Pavucontrol is not a forced dependency: if you want to use it then the button is there to help.

Note. When Vol2X-Reloaded opens the slider is always in zero position. Once the slider gets moved the sound levels start changing between 0% and 100%.

Keybindings:

Support for volume down and volume up keyboard keys. Pressing them should move the slider and change the sound level (-5% or +5%). Note. If you have something like Xbindkeys or anything else binding globally to volume keys, then the volume keys might not work in Vol2X-Reloaded.

Furthermore, pressing escape key (The ESC key from the keyboard) will quit the program.

______________________________

Executing:

If needed, make the python file executable:

chmod +x filename.py

Run with: python filename_location.py

_________________________

What happens to Vol2X-QT5?

There is nothing inherently wrong with Vol2X-QT5. The program works and it will continue to work. If you want to use it, then that is completely fine. Vol2X-QT5 is unlikely to receive functional upgrades at this point. Vol2X-Reloaded will be the one that gets new features and continues to develop further.

________________

Original post is at: http://www.techtimejourney.net/vol2x-reloaded-arrives/
