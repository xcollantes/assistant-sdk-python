import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BOARD)
pinON = 7
pinOFF = 11

GPIO.setup(pinON, GPIO.OUT, initial=0)
GPIO.setup(pinOFF, GPIO.OUT, initial=0)

def onoff(on):
    if on:
        print('Turning device on')
        burst(pinON, 1)
    else:
        print('Turning device off')
        burst(pinOFF, 1)
    GPIO.cleanup()


def burst(pin, seconds):
    GPIO.output(pin, 1)
    time.sleep(seconds)
    GPIO.output(pin, 0)


arg = sys.argv[1].upper()
print ('Arg passed: %s' %arg)
if arg == 'ON':
    onoff(True)
else:
    onoff(False)


GPIO.cleanup()
