# rpi_lab1.py
# This program will blink LED at fixed interval of 0.5sec

# Import Python library
import RPi.GPIO as GPIO
import time

# Pin  Definitons:
ledPin = 23 # LED connect to GPIO23

# Pin Setup:
GPIO.setmode(GPIO.BCM)       # Broadcom pin-numbering scheme
GPIO.setup(ledPin, GPIO.OUT) # LED pin set as output

# Main routine
print("Press CTRL+C to terminate program")
try:
    while 1:
	GPIO.output(ledPin, GPIO.HIGH) #set ouput pin to logic HIGH (3.3V)
	time.sleep(0.5)                # delay 0.5 sec
	GPIO.output(ledPin, GPIO.LOW)  #set ouput pin to logic LOW (0V)
	time.sleep(0.5)                # delay 0.5 sec

except KeyboardInterrupt: # Exit program if CTRL+C is pressed
    GPIO.cleanup()        # cleanup all GPIO and set all to input