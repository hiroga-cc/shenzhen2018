import requests
import time
import grovepi
import pygame


light_sensor = 2
cover_open = False

while True:
    try:
        # Get value from light sensor
        light_intensity = grovepi.analogRead(light_sensor)
        print(light_intensity)

        if light_intensity >= 120 and cover_open == False:
            cover_open = True
            print("Cover Open!")
        if light_intensity <= 120 and cover_open == True: 
            cover_open = False
            print("Cover Close!")
            pygame.mixer.init()
            pygame.mixer.music.load("jinglebellssms.mp3")
            pygame.mixer.music.play()

            try:
                r1 = requests.get(os.environ["SERVER_NAME"])
	        print(r1.status_code)
	        print(r1.json())
            except(ValueError):
                print("Maybe server is not runnnig XD")

        time.sleep(0.5)

    except IOError:
       print("Error")
    except TypeError:
       print("Error")
       # If IOError Occured, it become TypeError
