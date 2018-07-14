# coding: utf-8
import grovepi


class GarbageSensor():
    def __init__(self):
        # 光検知センサーをD2にセットすること
        self.light_sensor = 2
        self.cover_open = False

    def was_trash_thrown(self):
        try:
            light_intensity = grovepi.analogRead(self.light_sensor)
            print("Light Intensity: ", light_intensity)

            if light_intensity >= 120 and self.cover_open == False:
                self.cover_open = True
                print("Cover Open!")

            if light_intensity <= 120 and self.cover_open == True: 
                self.cover_open = False
                print("Cover Close!")
                return True

        except IOError:
            print("Error")
        except TypeError:
            print("Error")
            # IOErrorが発生した場合、GrovePiがTypeErrorとして投げる仕様になっている。(2018年5月現在)


if __name__ == "__main__":
    gs = GarbageSensor()
    while True:
        if True  == gs.was_trash_thrown():
            print("Trash was Thrown!!!")