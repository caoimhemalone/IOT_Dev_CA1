import dweepy, math, time, platform, random
from grovpi import *
from threading import Thread


#Add in port numbers
led1 = 
led2 = 
led3 = 
camera = #buzzer is set off when photo is taken along with the green LED
dht_sensor_port = 
buzzer = 
button = #button takes photo

publisher_state = False;
thing_from_pi = "CaoimhesThing"

def listener(publisher):
	for dweet in dweepy.listen_for_dweets_from('caoimhe'):
		content = dweet["content"]
		should_publish = content["publish"]
		print should_publish
		if should_publish == "true"
		# start the publisher thread
		global publisher_state
		publisher_state = True 
		if not publisher.is_alive():
			publisher = Thread(target=publisher_method_caoimhe)
		publisher.start()
	else:
		publisher_state = False
		print "Wasn't true"

def publisher_method_caoimhe():
	while publisher_state:
		#Code goes here

		def getTemp():
			try:
				[temp, hum] = dht(dht_sensor_port, 0)
				print "temp =", temp,
				if math.isnan(temp):
					temp = 0
				return float(temp)
			except(IOError, TypeError) as e:
				print "Error"

		def getHumidity():
			try: 
				[temp, hum] = dht(dht_sensor_port, 0)
				print "humidity =", hum, "%"
				if math.isnan(hum):
					hum =0
				return hum
			except (IOError, TypeError) as e:
				print "Error"

		#For camera
		def getCamera():
			try:
				button_status = digitalRead(button)
				if button_status:
					#take a picture
				else:
					#Nothing
					print("Camera is not active")
					return 0
			except (IOError, TypeError) as e:
				print ("Error")

		#For Blue led
		def getBlueLed():
			try:
				button_app_status1 = #the app
				if button_app_status1:
					digitalWrite(led, 1)
					print ("Blue LED On")
					return 1
				else:
					digitalWrite(led, 0)
					print("Blue LED Off")
					return 0
			except (IOError, TypeError) as e:
				print ("Error")

		#For Green led
		def getGreenLed():
			try:
				button_app_status2 = #the app
				if button_app_status2:
					digitalWrite(led, 1)
					print ("Green LED On")
					return 1
				else:
					digitalWrite(led, 0)
					print("Green LED Off")
					return 0
			except (IOError, TypeError) as e:
				print ("Error")

		#For Red led
		def getRedLed():
			try:
				button_app_status3 = #the app
				if button_app_status3:
					digitalWrite(led, 1)
					print ("Red LED On")
					return 1
				else:
					digitalWrite(led, 0)
					print("Red LED Off")
					return 0
			except (IOError, TypeError) as e:
				print ("Error")

	def post(dic):
    thing = 'Caoimhe Malone IOT Dev'
    print dweepy.dweet_for(thing, dic)

	def getReadings():
	    dict = {}
	    dict ["led1"] = getBlueLED()
	    dict ["led2"] = getGreenLED()
	    dict ["led3"] = getRedLED()
	    dict ["temperature"] = getTemp()
	    dict ["humidity"] = getHumidity()
	    dict ["camera"] = getCamera()
	    return dict

	while True:
	    dict = getReadings();
	    post(dict)
	    time.sleep(5)


	print "publishing ending"

	#dweepy code goes here post

publisher_thread = Thread(target=publisher_method_caoimhe)
listener_thread = Thread(target=listener, args=(publisher_thread,))
listener_thread.start()