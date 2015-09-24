# rpi_lab3.py 
# This program will monitor the status of the push button. 
# When it is pressed, cycle the brigthness of LED

# Import Python library
import RPi.GPIO as GPIO
import time

# Pin Definitons:
pwmPin = 23 # LED connect to GPIO23
butPin = 24 # Push button connect to GPIO24

dutyCycle = 0 # duty cycle of PWM output. Value=0.0 to 100.0

# Pin Setup:
GPIO.setmode(GPIO.BCM)          # Broadcom pin-numbering scheme
GPIO.setup(pwmPin, GPIO.OUT)    # PWM pin set as output
pwm = GPIO.PWM(pwmPin, 50)      # Initialize PWM on pwmPin 100Hz frequency

# Button pin set as input with internal pull-up
GPIO.setup(butPin, GPIO.IN, pull_up_down=GPIO.PUD_UP) 

# start PWM
pwm.start(dutyCycle)

print("Press CTRL+C to terminate program")
try:
    while 1:
        if GPIO.input(butPin) == False:  # button is pressed
	       if dutyCycle > 0:
	           dutyCycle = dutyCycle - 2 # reduce the value of duty cycle by step of 2
	       else: 
		       dutyCycle = 100           # reset the dutyCycle to 100 if it reaches 0

            pwm.ChangeDutyCycle(dutyCycle)
        time.sleep(0.1)                # delay 0.1 second
except KeyboardInterrupt:                # If CTRL+C is pressed, exit cleanly2
    pwm.stop()                           # stop PWM
    GPIO.cleanup()                       # cleanup all GPIO and set all to input