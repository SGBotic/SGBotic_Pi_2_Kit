# rpi_lab2.py 
# This program uses PWM output to change the brightness of each of the R, G and B LED, which in turn change the color.
# The PWM duty cycle is set by the randomly generated integral number between 1 to 100

# Import Python library
import RPi.GPIO as GPIO
import time
import random

# Pin Definitons:
redPin = 23 # Red pin connect to GPIO23
greenPin = 24 # Green pin connect to GPIO24
bluePin = 25 # Blue pin connect to GPIO25


dc = 0 # duty cycle of PWM output. Value=1 to 100

# Pin Setup:
GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme
GPIO.setup(redPin, GPIO.OUT) # LED pin set as output
GPIO.setup(greenPin, GPIO.OUT)
GPIO.setup(bluePin, GPIO.OUT)

pwm_red = GPIO.PWM(redPin, 100)     # Initialize PWM on redPin 100Hz frequency
pwm_green = GPIO.PWM(greenPin, 100) # Initialize PWM on greenPin 100Hz frequency
pwm_blue = GPIO.PWM(bluePin, 100)   # Initialize PWM on bluePin 100Hz frequency

# start PWM output
pwm_red.start(dc)
pwm_green.start(dc)
pwm_blue.start(dc)

print("Press CTRL+C to terminate program")
try:
    while 1:
       
        pwm_red.ChangeDutyCycle(random.randint(1, 100))     # Change the PWM duty cycle with random generated integral (value between 1 to 100)
	    pwm_green.ChangeDutyCycle(random.randint(1, 100))
	    pwm_blue.ChangeDutyCycle(random.randint(1, 100))
           
        time.sleep(0.1)
except KeyboardInterrupt: # Exit program if CTRL+C is pressed
    pwm_red.stop() # stop PWM
    pwm_green.stop() # stop PWM
    pwm_blue.stop() # stop PWM
    GPIO.cleanup() # set all GPIO to input