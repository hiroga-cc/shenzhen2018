# coding: utf-8
import Image
import select
import time

import v4l2capture
import zbar

from qrcode_decoder import QrcodeDecoder
from addr import AddrHandler

class QrcodeReader():
    def __init__(self):
        # Videoデバイスを開く。
        self.video = v4l2capture.Video_device("/dev/video0")

        # image sizeを提案する。`v4l2-ctl --all`などのコマンドで調べられる。
        # RGB3またはYUYV以外は指定可能なのか？
        self.video.set_format(640, 480, fourcc="RGB3")
        self.size_x, self.size_y, self.fourcc = self.video.get_format()
        print self.size_x, self.size_y, self.fourcc

        # QRコードDecoder(zbarのラッパー)
        self.decoder = QrcodeDecoder()

        # アドレス格納用クラス
        self.addr = AddrHandler()

    def capture_once(self):
        try:
            # バッファーの作成。画像の場合は1でよく、動画だと30など。fpsに相当するのか？
            self.video.create_buffers(1)

            # デバイスにバッファーを送る。
            self.video.queue_all_buffers()

            # USBカメラのLEDが点灯する。
            self.video.start()

            # デバイスがバッファーを満たすまで待機。
            select.select((self.video,), (), ())
            image_data = self.video.read()
            self.video.stop()
            self.video.close()
            pil = Image.frombuffer("RGB", (self.size_x, self.size_y), image_data)
            pil.save("images/smile.jpg")
            symbol = self.decoder.decode_bytes(self.size_x, self.size_y, "Y800", pil.convert("L").tobytes())
            print "symbol", symbol
            return symbol

        finally:
            self.video.close()

    def capture_forever(self):
        try:
            self.video.create_buffers(1)

            while True:
                self.video.queue_all_buffers()
                self.video.start()
                select.select((self.video,), (), ())
                image_data = self.video.read_and_queue()
                pil = Image.frombuffer("RGB", (self.size_x, self.size_y), image_data)
                pil.save("images/smile.jpg") # 本番ではコメントアウト
                symbol = self.decoder.decode_bytes(self.size_x, self.size_y, "Y800", pil.convert("L").tobytes())
                print "symbol", symbol
                if symbol is not None:
                    self.addr.write_addr(symbol)
                self.video.stop()

        finally:
            self.video.close()


if __name__ == "__main__":
    r = QrcodeReader()
    try: 
        r.video.create_buffers(1)
        r.video.queue_all_buffers()
        r.video.start()
        print "Smile! 3 2 1..."
        time.sleep(3)
        select.select((r.video,), (), ())
        image_data = r.video.read()
        r.video.close()
        image = Image.frombuffer("L", (r.size_x, r.size_y), image_data)
        image.save("images/smile.jpg")
    finally:
        r.video.close()