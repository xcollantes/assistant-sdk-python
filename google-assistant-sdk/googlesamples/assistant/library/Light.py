#! env/bin/python

# Xavier Collantes
# 10/14/2018
# Light Class for IoT room lights

import time
import logging
import RPi.GPIO as GPIO



# Added from https://developers.google.com/assistant/sdk/guides/library/python/extend/handle-device-commands
def _turn(command, params):
    if command == "action.devices.commands.OnOff":
        if params['on']:
            print('Turning the LED on.')
        else:
            print('Turning the LED off.')

def onoff(on):
    pinON = 7
    pinOFF = 11
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pinON, GPIO.OUT, initial=0)
    GPIO.setup(pinOFF, GPIO.OUT, initial=0)

    def burst(pin, seconds=0.5):
        GPIO.output(pin, 1)
        time.sleep(seconds)
        GPIO.output(pin, 0)

    if on:
        logging.info('Turning device on')
        burst(pinON)
    else:
        logging.info('Turning device off')
        burst(pinOFF)
    GPIO.cleanup()

