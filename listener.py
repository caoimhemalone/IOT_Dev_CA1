import dweepy, time, random, math, picamera
from grovepi import *
from time import sleep, gmtime, strftime
from threading import Thread



# #START OF AWS CODE
'''
/*
 * Copyright 2010-2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License").
 * You may not use this file except in compliance with the License.
 * A copy of the License is located at
 *
 *  http://aws.amazon.com/apache2.0
 *
 * or in the "license" file accompanying this file. This file is distributed
 * on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
 * express or implied. See the License for the specific language governing
 * permissions and limitations under the License.
 */
 '''

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import sys
import logging
import time
import getopt

# Custom MQTT message callback
def customCallback(client, userdata, message):
    print("Received a new message: ")
    print(message.payload)
    print("from topic: ")
    print(message.topic)
    print("--------------\n\n")
    reply = message

# Usage
usageInfo = """Usage:

Use certificate based mutual authentication:
python basicPubSub.py -e <endpoint> -r <rootCAFilePath> -c <certFilePath> -k <privateKeyFilePath>

Use MQTT over WebSocket:
python basicPubSub.py -e <endpoint> -r <rootCAFilePath> -w

Type "python basicPubSub.py -h" for available options.
"""
# Help info
helpInfo = """-e, --endpoint
    Your AWS IoT custom endpoint
-r, --rootCA
    Root CA file path
-c, --cert
    Certificate file path
-k, --key
    Private key file path
-w, --websocket
    Use MQTT over WebSocket
-h, --help
    Help information


"""

# Read in command-line parameters
useWebsocket = False
host = "a17y717e4a92so.iot.us-east-1.amazonaws.com"
rootCAPath = "root.pem"
certificatePath = "cert.pem.crt"
privateKeyPath = "private.pem.key"
try:
#   opts, args = getopt.getopt(sys.argv[1:], "hwe:k:c:r:", ["help", "endpoint=", "key=","cert=","rootCA=", "websocket"])
#   if len(opts) == 0:
#       raise getopt.GetoptError("No input parameters!")
#   for opt, arg in opts:
#       if opt in ("-h", "--help"):
#           print(helpInfo)
#           exit(0)
#       if opt in ("-e", "--endpoint"):
#           host = arg
#       if opt in ("-r", "--rootCA"):
#           rootCAPath = arg
#       if opt in ("-c", "--cert"):
#           certificatePath = arg
#       if opt in ("-k", "--key"):
#           privateKeyPath = arg
#       if opt in ("-w", "--websocket"):
#           useWebsocket = True
# except getopt.GetoptError:
#   print(usageInfo)
#   exit(1)

# Missing configuration notification
# missingConfiguration = False
# if not host:
#   print("Missing '-e' or '--endpoint'")
#   missingConfiguration = True
# if not rootCAPath:
#   print("Missing '-r' or '--rootCA'")
#   missingConfiguration = True
# if not useWebsocket:
#   if not certificatePath:
#       print("Missing '-c' or '--cert'")
#       missingConfiguration = True
#   if not privateKeyPath:
#       print("Missing '-k' or '--key'")
#       missingConfiguration = True
# if missingConfiguration:
#   exit(2)

# Configure logging
logger = logging.getLogger("AWSIoTPythonSDK.core")
logger.setLevel(logging.DEBUG)
streamHandler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

# # Init AWSIoTMQTTClient
myAWSIoTMQTTClient = None
if useWebsocket:
    myAWSIoTMQTTClient = AWSIoTMQTTClient("basicPubSub", useWebsocket=True)
    myAWSIoTMQTTClient.configureEndpoint(host, 443)
    myAWSIoTMQTTClient.configureCredentials(rootCAPath)
else:
    myAWSIoTMQTTClient = AWSIoTMQTTClient("basicPubSub")
    myAWSIoTMQTTClient.configureEndpoint(host, 8883)
    myAWSIoTMQTTClient.configureCredentials(rootCAPath, privateKeyPath, certificatePath)

# AWSIoTMQTTClient connection configuration
myAWSIoTMQTTClient.configureAutoReconnectBackoffTime(1, 32, 20)
myAWSIoTMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myAWSIoTMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myAWSIoTMQTTClient.configureConnectDisconnectTimeout(10)  # 10 sec
myAWSIoTMQTTClient.configureMQTTOperationTimeout(5)  # 5 sec

# Connect and subscribe to AWS IoT
myAWSIoTMQTTClient.connect()
myAWSIoTMQTTClient.subscribe("sdk/test/Python", 1, customCallback)
time.sleep(2)
# END OF AWS CODE

output = strftime("/home/pi/Desktop/IOT_Dev_CA1/Pi_Photos/img-%d-%m %H:%M:%S.png", gmtime())

sleep_time = time

led1sensor = 3
led2sensor = 8
led3sensor = 4
#camera = #buzzer is set off when photo is taken along with the green LED
camera = picamera.PiCamera()
dht_sensor_port = 7
buzzer = 5

led1_state = False;
led2_state = False;
led3_state = False;
cam_state = False;
temp_state = False;
# hum_state = False;
thingName = "caoimhe"


def listener(led1, led2, led3, cam, temp):
        for dweet in dweepy.listen_for_dweets_from('caoimhe'):
                content = dweet["content"]
                should_publish = content.get("publish", "")
                print should_publish
                sleep_time = content.get("time", "")
                global  led1_state, led2_state, led3_state, cam_state, temp_state
                if should_publish == "true":
                        # show hum and temp
                            temp_state = True
                            if not publisher.is_alive():
                                publisher = Thread(target=Temp_Method)
                                publisher.start()
                if should_publish == "led1":
                        # start the publisher thread
                        led1_state = True
                        if not led1.is_alive():
                                led1 = Thread(target=Blue_Method)
                        led1.start()
                elif should_publish == "led2":
                        # start the publisher thread
                        led2_state = True
                        if not led2.is_alive():
                                led2 = Thread(target=Green_Method)
                        led2.start()
                elif should_publish == "led3":
                        # start the publisher thread
                        led3_state = True
                        if not led3.is_alive():
                                led3 = Thread(target=Red_Method)
                        led3.start()
                elif should_publish == "cam":
                        # start the publisher thread
                        cam_state = True
                        if not cam.is_alive():
                                cam = Thread(target=Camera_Method)
                        cam.start()
                elif should_publish == "temp":
                        # start the publisher thread
                        temp_state = True
                        if not temp.is_alive():
                                temp = Thread(target=Temp_Method)
                        temp.start()
                # elif should_publish == "hum":
                #         # start the publisher thread
                #         hum_state = True
                #         if not hum.is_alive():
                #                 hum = Thread(target=Hum_Method)
                #         hum.start()

                else:
                        #publisher_state = False
                        led1_state = False;
                        led2_state = False;
                        led3_state = False;
                        cam_state = False;
                        temp_state = False;
                        # hum_state = False;

                        print "Wasn't true"

            #Sensor Code 

#For camera
def Camera_Method():
    while cam_state:
        try:
                #take a picture
                digitalWrite(buzzer, 1)
               # time.sleep(0.05)
                digitalWrite(buzzer,0)
                digitalWrite(led2sensor, 1)
                camera.capture(output)
                print("Photo Taken")
                camera.start_preview()
                camera.vflip = True
                camera.hflip = True
                camera.brightness = 60

                digitalWrite(led2sensor, 0)
                digitalWrite(buzzer, 0)
                result = dweepy.dweet_for('raspberryPI', {"camera": 1})
                print result
                time.sleep(5)

        except (IOError, TypeError) as e:
            digitalWrite(led2sensor,0)
            digitalWrite(buzzer, 0)
            print "Error"
        except KeyboardInterrupt:
                digitalWrite(led2sensor,0)
                digitalWrite(buzzer, 0)
        break

    print "Cam ending"

#For Blue LED
def Blue_Method():
    while led1_state:
        try:
            digitalWrite(buzzer, 1)
            time.sleep(.5)
            digitalWrite(buzzer, 0)
            digitalWrite(led1sensor, 1)
            print ("Blue LED On")
            result = dweepy.dweet_for('raspberryPI', {"led1": 1})
            print result
            time.sleep(sleep_time)

            digitalWrite(led1sensor, 0)
            digitalWrite(buzzer, 0)
            print ("Blue LED Off")
            result = dweepy.dweet_for('raspberryPI', {"led1": 0})
            print result
            time.sleep(sleep_time)

        except KeyboardInterrupt:
                digitalWrite(led1sensor,0)
                digitalWrite(buzzer, 0)
                break

        except (IOError, TypeError) as e:
            digitalWrite(led1sensor,0)
            digitalWrite(buzzer, 0)

            print e
          
        print "Blue LED ending"

#For Green LED
def Green_Method():
    while led2_state:
        try:
            digitalWrite(buzzer, 1)
            time.sleep(.5)
            digitalWrite(buzzer, 0)
            digitalWrite(led2sensor, 1)
            print ("Green LED On")
            result = dweepy.dweet_for('raspberryPI', {"led2": 1})
            print result
            time.sleep(sleep_time)

            digitalWrite(led2sensor, 0)
            print ("Green LED Off")
            result = dweepy.dweet_for('raspberryPI', {"led2": 0})
            print result
            time.sleep(sleep_time)

        except KeyboardInterrupt:
                digitalWrite(led2sensor,0)
                digitalWrite(buzzer, 0)
                break

        except (IOError, TypeError) as e:
            digitalWrite(led2sensor,0)
            digitalWrite(buzzer, 0)
            print "Error"
        print "Green LED ending"

#For Red LED
def Red_Method():
    while led3_state:
        try:
            
            digitalWrite(buzzer, 1)
            time.sleep(.5)
            digitalWrite(buzzer, 0)
            digitalWrite(led3sensor, 1)
            print ("Red LED On")
            result = dweepy.dweet_for('raspberryPI', {"led3": 1})
            print result
            time.sleep(sleep_time)

            digitalWrite(led3sensor, 0)
            print ("Red LED Off")
            result = dweepy.dweet_for('raspberryPI', {"led3": 0})
            print result
            time.sleep(sleep_time)

        except KeyboardInterrupt:
                digitalWrite(led3sensor,0)
                digitalWrite(buzzer, 0)
                break

        except (IOError, TypeError) as e:
            digitalWrite(led3sensor,0)
            digitalWrite(buzzer, 0)
            print "Error"
        print "Red LED ending"

#For temp
def Temp_Method():
    while temp_state:
        try:
            [temp, hum] = dht(dht_sensor_port, 0)
            print "temp =", temp,
            if math.isnan(temp):
                temp = 0
            return float(temp)
        except (IOError, TypeError) as e:
            print "Error"

# #For Hum
# def Hum_Method():
#     while hum_state:
#         try:
#             [temp, hum] = dht(dht_sensor_port, 0)
#             print "humidity =", hum, "%"
#             if math.isnan(hum):
#                 hum =0
#             return hum
#         except (IOError, TypeError) as e:
#             print "Error"


#publisher_thread = Thread(target=publisher_method_caoimhe)
led1_thread = Thread(target=Blue_Method)
led2_thread = Thread(target=Green_Method)
led3_thred = Thread(target=Red_Method)
cam_thread = Thread(target=Camera_Method)
temp_thread = Thread(target=Temp_Method)
#hum_thread = Thread(target=Hum_Method)

listener_thread = Thread(target=listener, args=(led1_thread, led2_thread, led3_thred, cam_thread,temp_thread,))
listener_thread.start()
