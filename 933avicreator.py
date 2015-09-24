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

logging.basicConfig(format = '%(levelname)-8s [%(asctime)s] %(message)s', level = logging.INFO, filename = '933avicreator.log')

#Current utc date & time
name = datetime.utcnow()

#Go to directory
path = "/mnt/flash/prepare933"
os.chdir(path)

#Make & start command to convert jpg to avi
comname = "avconv -r 5 -i %06d.jpg -r 5 -vcodec mjpeg -qscale 1 .avi"
result = subprocess.getoutput(comname)
logging.info('AVI created!')

#Rename .avi to current_utc_date_time.avi
f = os.listdir(path)
#vid = glob.glob('.avi')
ren = os.rename('.avi', str(name)+'.avi')
logging.info('___Exit from script___')


#////////////////////////////
#path = "/home/pi/scripts"
#os.chdir(path)
#f = open('index','r')
#f.readline(i)
#print(i)
#f.close()

#i=i+1

#f = open('index','w')
#f.write(str(i) + '\n')
#print(i)
#f.close()
#//////////////////////////


