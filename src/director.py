# coding: utf-8
import time
import pygame


class Director():
    def __init__(self):
        pygame.mixer.init()
        pygame.mixer.music.load("jinglebellssms.mp3")
        
    def play(self):
        print("Start Playing")
        pygame.mixer.music.play()


if __name__ =="__main__":
    d = Director()
    d.play()

    # 音楽をplay()するより先にPythonが終了すると、音楽が再生されない/途中で終了するため。
    time.sleep(3)