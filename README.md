# Vol2X-Reloaded
Vol2X-Reloaded is an application for controlling Linux volume levels.

![vol2x](https://user-images.githubusercontent.com/29865797/194320780-3fa91e2b-d613-49b4-941d-983d57ccc2b3.png)

#Vol2X-Reloaded v.2 Copyright (c) 2017 JJ Posti <techtimejourney.net>#Vol2X-Reloaded comes with ABSOLUTELY NO WARRANTY;#for details see: http://www.gnu.org/copyleft/gpl.html. #This is free software, and you are welcome to redistribute it under #GPL Version 2, June 1991″

_____________

Dependencies:

pulseaudio #this is a must-have dependency.

pulseudio-utils #this is needed because the program uses pactl.

alsa-utils #this is needed because the program uses amixer as a helper when fetching system sound level upon start. Amixer is also used when setting microphone input level via the microphone slider.

pavucontrol #optional dependency.

python-pyqt5
python3-pyqt5 python
python3

The actual package names might differ depending on the system. Furthermore, python should be installed by default in most system. In reality the only package that you might need to install, in regard to python, is python-pyqt5 or similar.

__________________

Executing:

After downloading, decompress the archive and cd into the Vol2X directory.

If needed, make python files executable:

chmod +x filename.py

Note. The main executable is called vol2x.py .

Run with: python filename_location.py

___________________________

Vol2x-Reloaded 2.2.0 upgrade(October 2022):
Vol2x-Reloadded is upgraded. It gains awareness of system sound & microphone levels. 

Vol2X-Reloaded features:

Since v.2:

-Slider to control microphone input level: this only works for the main microphone. In the case of multiple inputs(microphones), you can turn them off with pavucontrol. Turning unnecessary microphones off makes sure that you are controlling the desired one with the slider.

Notice that both sliders connect to same lcd. The lcd value will change accordingly, depending on which slider you move.

-Vol2X-Reloaded can now fetch system volume when it starts. Slider and lcd display will both be set to the current system volume from the start.

-Button highlighting is added. This feature activates when mouse hovers over buttons.

-Code has cleaned up significantly.

-Volume levels from 0-100% and microphone volumes now live in their own module(volChange.py) and come into the main program as static class methods. I have also enhanced the code commenting further.

Since v.1:

-Slider that lets you control 5 devices. This means that the volume will change from your Bluetooth, HDMI or regular sound device etc. when the slider is moved.

-Buttons with tooltips. Button pressing changes slider position as well.

-Has a button for Pavucontrol in case more sound management is needed. Pavucontrol is not a forced dependency: if you want to use it then the button is there to help.

__________________

Keybindings:

Support for volume down and volume up keyboard keys. Pressing them should move the slider and change the sound level (-5% or +5%). Note. If you have something like Xbindkeys or anything else binding globally to volume keys, then the volume keys might not work in Vol2X-Reloaded.

Furthermore, pressing escape key (The ESC key from the keyboard) will quit the program.

_______________________

Original post is at: http://www.techtimejourney.net/vol2x-reloaded-v-2/
