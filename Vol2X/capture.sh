#!/bin/bash
#Microphone
awk -F"[][]" '/Left:/ { print $2 }' <(amixer sget Capture) | tr -d '[]%'
