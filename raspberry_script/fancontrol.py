#!/usr/bin/env python3

import RPi.GPIO as GPIO            # import RPi.GPIO module
from time import sleep             # lets us have a delay
import re, subprocess

fanpin = 16
GPIO.setmode(GPIO.BCM)             # choose BCM or BOARD
GPIO.setup(fanpin, GPIO.OUT)       # set GPIO16 as an output
pi_pwm = GPIO.PWM(fanpin,120)     # create PWM instance with frequency
pi_pwm.start(0)                    # start PWM of required Duty Cycle

def check_CPU_temp():
    temp = None
    err, msg = subprocess.getstatusoutput('vcgencmd measure_temp')
    if not err:
        m = re.search(r'-?\d\.?\d*', msg)   # a solution with a  regex
        try:
            temp = float(m.group())
        except ValueError: # catch only error needed
            pass
    return temp, msg

temp, msg = check_CPU_temp()
temp = int(temp)
#print(temp)



try:
    while True:
        if temp > 70:
            pi_pwm.ChangeDutyCycle(100)
            sleep(5)                 # wait five second
            temp, msg = check_CPU_temp()
            temp = int(temp)
            print(str(temp) + " 100%")
        elif temp > 60 and temp <= 70:
            pi_pwm.ChangeDutyCycle(80)
            sleep(5)                 # wait five second
            temp, msg = check_CPU_temp()
            temp = int(temp)
            print(str(temp) + " 80%")
        elif temp >= 50 and temp <= 60:
            pi_pwm.ChangeDutyCycle(60)
            sleep(5)                 # wait five second
            temp, msg = check_CPU_temp()
            temp = int(temp)
            print(str(temp) + " 60%")
        else:
            pi_pwm.ChangeDutyCycle(0)
            sleep(5)                 # wait five second
            temp, msg = check_CPU_temp()
            temp = int(temp)
            print(str(temp) + " 0%")
except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt
    GPIO.cleanup()                 # resets all GPIO ports used by this program
