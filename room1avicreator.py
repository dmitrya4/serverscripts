#!/usr/bin/python3

import re
import os
import sys
import cmd
import subprocess
import fileinput
import glob
import logging
from datetime import datetime, date, time

logging.basicConfig(format = '%(levelname)-8s [%(asctime)s] %(message)s', level = logging.INFO, filename = 'room1avicreator.log')

#Current UTC date & time
name = datetime.utcnow()
#logging.info(name)

#Go to directory
path = "/mnt/flash/prepareroom1"
os.chdir(path)

#Make & start command to convert jpg to avi
comname = "avconv -r 5 -i %06d.jpg -r 5 -vcodec mjpeg -qscale 1 .avi"
result = subprocess.getoutput(comname)
logging.info(comname)

#Rename .avi to current_utc_date_time.avi
f = os.listdir(path)
ren = os.rename('.avi', str(name)+'.avi')
logging.info('Finished')
logging.info('_____________________________')


