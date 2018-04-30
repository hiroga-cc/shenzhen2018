import time
import os
import tinys3
from grovepi import *

# 事前にS3のバケット設定、IAMユーザー設定、それらのキーの環境変数への設定が必要
conn = tinys3.Connection(os.environ["S3_ACCESS_KEY"], os.environ["S3_SECRET_KEY"], tls=True)

button = 4

pinMode(button, "INPUT")
while True:
    try:
        if digitalRead(button):
            print("PUSH!!")
            os.system('fswebcam -r 320x240 -S 3 --jpeg 50 --save /home/pi/to_transmit/photo.jpg')
            f = open('/home/pi/to_transmit/photo.jpg','rb')
            conn.upload('photo.jpg',f, os.environ["S3_BUCKET_NAME"])
            time.sleep(30)

    except (IOError, TypeError) as e:
        print(e) 
