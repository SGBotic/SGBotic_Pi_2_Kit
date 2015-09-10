# rpi_lab3.py 
# This program will monitor the status of the push button. When it is pressed, cycle the brigthness of LED

# Import Python library
import RPi.GPIO as GPIO
import time

# Pin Definitons:
pwmPin = 23 # LED connect to GPIO23
butPin = 24 # Push button connect to GPIO24

dc = 100 # duty cycle (0-100) of PWM pin 

# Pin Setup:
GPIO.setmode(GPIO.BCM)          # Broadcom pin-numbering scheme
GPIO.setup(pwmPin, GPIO.OUT)    # PWM pin set as output
pwm = GPIO.PWM(pwmPin, 50)      # Initialize PWM on pwmPin 100Hz frequency
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Button pin set as input with internal pull-up

# start PWM
pwm.start(dc)

print("Press CTRL+C to terminate program")
try:
    while 1:
        if GPIO.input(butPin) == False: # button is pressed
	       if dc > 0:
	           dc = dc - 2     # change the value of duty cycle
	       else: 
		       dc = 100

            pwm.ChangeDutyCycle(100-dc)
        time.sleep(0.075)
except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly2
    pwm.stop() # stop PWM
    GPIO.cleanup() # cleanup all GPIO