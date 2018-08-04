# coding: utf-8
import time
import pygame


class Director():
    def __init__(self):
        pygame.mixer.init()

    def play_decoded(self):
        pygame.mixer.music.load("sounds/address_big.mp3")
        pygame.mixer.music.play()
        
    def play_thanks(self):
        print("Start Playing")
        pygame.mixer.music.load("sounds/payment_thanks_big.mp3")
        pygame.mixer.music.play()
	time.sleep(5)

        pygame.mixer.music.load("sounds/jinglebellssms.mp3")
        pygame.mixer.music.play()

    def play_error(self):
        pygame.mixer.music.load("sounds/error_big.mp3")
        pygame.mixer.music.play()

if __name__ =="__main__":
    d = Director()
    d.play()

    # 音楽をplay()するより先にPythonが終了すると、音楽が再生されない/途中で終了するため。
    time.sleep(3)
