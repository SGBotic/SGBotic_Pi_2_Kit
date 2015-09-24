# rpi_lab4.py
# Distance measurement using HC-SR05 v2 ultrasonic sensor

# Import Python libraries
import time
import RPi.GPIO as GPIO

# Pin Definitons:
sonarTrigger = 27   # Trigger pin connect to GPIO27
sonarEcho = 17      # Echo pin connect to GPIO17

# Pin Setup
GPIO.setmode(GPIO.BCM)
GPIO.setup(sonarTrigger,GPIO.OUT)  # Trigger
GPIO.setup(sonarEcho,GPIO.IN)      # Echo

# Set trigger pin to Low
GPIO.output(sonarTrigger, GPIO.LOW)

# Allow module to settle
time.sleep(0.5)

print("Press CTRL+C to terminate program")
try: 
   while 1:

    # Send 10us pulse to trigger
	GPIO.output(sonarTrigger, GPIO.HIGH)
	time.sleep(0.00001)
	GPIO.output(sonarTrigger, GPIO.LOW)
	start = time.time()

	#Listen to the echo pin. 0 means nothing is happening. 
    #Once a signal is received, record the time
	while GPIO.input(sonarEcho)==0:
  	   tBegin = time.time()
	while GPIO.input(sonarEcho)==1:
  	   tEnd = time.time()

	# Work out the time elapsed to calculate the distance
	timepassed = tEnd - tBegin

	# Convert the distance into centimeter by 
	# multiplied elapsed time with speed of sound (cm/s)
	distance = timepassed * 34000 / 2

	print "Distance : %.1f" % distance
	time.sleep(0.1)   # Delay 0.1 second

except KeyboardInterrupt: # Exit while loop if CTRL+C is pressed
	GPIO.cleanup()        # cleanup all GPIO and set all to input