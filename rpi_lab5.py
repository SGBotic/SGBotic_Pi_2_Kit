# rpi_lab5.py
# In this lab, we will will look at how to read temperatue and humidity value from DHT11 sensor and post the data
# to thingspeak.com, an Iot cloud service.
#
# You can see our channel at https://thingspeak.com/channels/54511 

# Import Python libraries
import httplib, urllib
import Adafruit_DHT
import time

pin = 23  #connect DHT11's output to GPIO23

sleep = 30      # delay between posts to the thingspeak.com (in second)
key = 'XB3N0MM3KWYDSIOQ'  # Thingspeak's API key (replace it with your own API key)

#Data log temperature and humidity value to Thingspeak Channel
def datalog():
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, pin)
	if humidity is not None and temperature is not None:
           print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
	   params = urllib.urlencode({'field1': temperature,'field2': humidity,'key':key }) 
	   
           headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
           conn = httplib.HTTPConnection("api.thingspeak.com:80")
           try:
               conn.request("POST", "/update", params, headers)
               response = conn.getresponse()
               print temperature
	       print humidity
               print response.status, response.reason
               data = response.read()
               conn.close()
           except:
               print "connection to ThingSpeak.com failed"	
    	   break
 	else:
	   print 'Failed to get DHT11 reading. Try again!'


#sleep for desired amount of time
if __name__ == "__main__":
        while True:
                datalog()
                time.sleep(sleep)
                