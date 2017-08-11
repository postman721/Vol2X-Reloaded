
#!/bin/sh
#This script is used to get the initial volume level to Vol2X-Reloaded when it starts.

amixer get Master | grep "%" | cut -d ' ' -f 7 | uniq | tr -cd [:digit:]
