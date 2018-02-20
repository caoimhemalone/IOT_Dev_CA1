import dweepy, time, random, math, picamera
from grovepi import *
from time import sleep, gmtime, strftime
from threading import Thread


output = strftime("/home/pi/Desktop/IOT_Dev_CA1/Pi_Photos/img-%d-%m %H:%M:%S.png", gmtime())

# sleep_time = 5

led1sensor = 7
led2sensor = 8
led3sensor = 5
#camera = #buzzer is set off when photo is taken along with the green LED
camera = picamera.PiCamera()
#dht_sensor_port = 0
buzzer = 3
#button = 2 #button takes photo

#publisher_state = False;
led1_state = False;
led2_state = False;
led3_state = False;
cam_state = False;
thingName = "caoimhe"


def listener(led1, led2, led3, cam):
        for dweet in dweepy.listen_for_dweets_from('caoimhe'):
                content = dweet["content"]
                should_publish = content.get("publish", "")
                print should_publish
                global  led1_state, led2_state, led3_state, cam_state, every_state
                # if should_publish == "true":
                #         # start the publisher thread
                #             publisher_state = True
                #             if not publisher.is_alive():
                #                 publisher = Thread(target=publisher_method_caoimhe)
                #                 publisher.start()
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

                else:
                        #publisher_state = False
                        led1_state = False;
                        led2_state = False;
                        led3_state = False;
                        cam_state = False;

                        print "Wasn't true"

# def publisher_method_caoimhe():
#     while publisher_state:
#         result = dweepy.dweet_for('raspberryPI', )
#         print result
#         time.sleep(5)
#     print "publishing ending"
           


            #Sensor Code 

#For camera
def Camera_Method():
    while cam_state:
        try:
                #take a picture
                digitalWrite(buzzer, 1)
                time.sleep(0.05)
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
            time.sleep(5)
            #digitalWrite(buzzer, 0)
            digitalWrite(led1sensor, 1)
            print ("Blue LED On")
            result = dweepy.dweet_for('raspberryPI', {"led1": 1})
            print result
            time.sleep(5)

            digitalWrite(led1sensor, 0)
            digitalWrite(buzzer, 0)
            print ("Blue LED Off")
            result = dweepy.dweet_for('raspberryPI', {"led1": 0})
            print result
            time.sleep(5)

        except KeyboardInterrupt:
                digitalWrite(led1sensor,0)
                digitalWrite(buzzer, 0)
                break

        except (IOError, TypeError) as e:
                print e
        print "Blue LED ending"

#For Green LED
def Green_Method():
    while led2_state:
        try:
            digitalWrite(led2sensor, 1)
            digitalWrite(buzzer, 1)
            time.sleep(5)
            digitalWrite(buzzer, 0)
            print ("Green LED On")
            result = dweepy.dweet_for('raspberryPI', {"led2": 1})
            print result
            time.sleep(5)

            digitalWrite(led2sensor, 0)
            print ("Green LED Off")
            result = dweepy.dweet_for('raspberryPI', {"led2": 0})
            print result
            time.sleep(5)

        except KeyboardInterrupt:
                digitalWrite(led2sensor,0)
                digitalWrite(buzzer, 0)
                break

        except (IOError, TypeError) as e:
                print "Error"
        print "Green LED ending"

#For Red LED
def Red_Method():
    while led3_state:
        try:
            digitalWrite(led3sensor, 1)
            digitalWrite(buzzer, 1)
            time.sleep(5)
            digitalWrite(buzzer, 0)
            print ("Red LED On")
            result = dweepy.dweet_for('raspberryPI', {"led3": 1})
            print result
            time.sleep(5)

            digitalWrite(led3sensor, 0)
            print ("Red LED Off")
            result = dweepy.dweet_for('raspberryPI', {"led3": 0})
            print result
            time.sleep(5)

        except KeyboardInterrupt:
                digitalWrite(led3sensor,0)
                digitalWrite(buzzer, 0)
                break

        except (IOError, TypeError) as e:
                print "Error"
        print "Blue LED ending"


#publisher_thread = Thread(target=publisher_method_caoimhe)
led1_thread = Thread(target=Blue_Method)
led2_thread = Thread(target=Green_Method)
led3_thred = Thread(target=Red_Method)
cam_thread = Thread(target=Camera_Method)

listener_thread = Thread(target=listener, args=(led1_thread, led2_thread, led3_thred, cam_thread,))
listener_thread.start()
