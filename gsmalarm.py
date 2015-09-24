#!/usr/bin/python2.7
import sys
import RPi.GPIO as GPIO
import serial
import time
import subprocess
import logging

ch_in = 5;

logging.basicConfig(format = '%(levelname)-8s [%(asctime)s] %(message)s', level = logging.INFO, filename = '/home/pi/scripts/gsmalarm.log')

port = serial.Serial("/dev/ttyAMA0", baudrate = 9600, timeout = 2)
start = "AT"
echooff = "ATE0"
cmgfset = "AT+CMGF=1"
cscsset = "AT+CSCS=\"GSM\""
dial1 = "ATD>1;" #My number
dial2 = "ATD>2;" #Tatyana number
endcall = "ATH"
smsnumber1 = "AT+CMGS=\"+79307040757\""
sms = "ALARM! GAS LEVEL IS OUT OF RANGE!"

#Send sms for me and Tatyana
#def sendsms():
#    port.write(smsnumber1+"\r\n")
#    time.sleep(0.2)
#    port.write(sms+chr(26)) #Send text and ctrl-z
#    time.sleep(0.2)

#Three times call me and Tatyana


#read = port.read()
#print read
#    port.close()

def main():
  GPIO.setmode(GPIO.BCM)
  GPIO.setwarnings(False)
  GPIO.setup(ch_in, GPIO.IN)
  GPIO.add_event_detect(ch_in, GPIO.RISING)


if __name__=='__main__':
    main()

while True:
  if GPIO.event_detected(ch_in):
    port.open()
    port.write(start+"\r\n")
    time.sleep(0.2)
    port.write(echooff+"\r\n")
    time.sleep(0.2)
    port.write(cmgfset+"\r\n")
    time.sleep(0.2)
    port.write(cscsset+"\r\n")
    time.sleep(0.2)
    logging.info('Neoway ready!')
    for i in range(3):
      port.write(dial1+"\r\n")
      time.sleep(20)
      port.write(endcall+"\r\n")
      time.sleep(10)
      logging.info('Call = OK, end Call = OK')
    port.close()



