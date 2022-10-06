
#!/bin/sh
#This script is used to get the initial volume level to Vol2X-Reloaded when it starts.

#Volume level
awk -F"[][]" '/Left:/ { print $2 }' <(amixer sget Master) | tr -d '[]%'

