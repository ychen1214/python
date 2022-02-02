"""Alarm Clock
-------------------------------------------------
"""

import datetime
import os 
import time 
import random
import webbrowser

def check_alarm_input(alarm_time):
    """Checks to see if the user has entered in a valid alarm time"""
    if len(alarm_time) == 1:
        if alarm_time[0] < 24 and alarm_time[0] >= 0:
            return True
    if len(alarm_time) == 2: 
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
            alarm_time[1] < 60 and alarm_time[1] >= 0:
            return True 
    elif len(alarm_time) == 3:
        if alarm_time[0] < 24 and alarm_time[0] >= 0 and \
            alarm_time[1] < 60 and alarm_time[1] >= 0 and \
            alarm_time[2] < 60 and alarm_time[2] >= 0:
            return True            
#check for urls existence.
if not os.path.isfile("youtube_alarm_videos.txt"):
    print('Creating "youtube file"....')
    with open("youtube_alarm.videos.txt","w") as alarm_file:
        alarm_file.write("https://www.youtbue.com")

#User Input for Alarm

