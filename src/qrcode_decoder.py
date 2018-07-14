# coding: utf-8
import zbar
from PIL import Image

class QrcodeDecoder():
    def __init__(self):
        self.scanner = zbar.ImageScanner()
        self.scanner.parse_config("enable")

    # receive QRCode file path and return first decoded symbol
    def decode_file(self, img_path):
        if type(img_path) != str or len(img_path) < 1:
            print "Path format wrong."
            return None

        try:
            # path from execution current path
            pil = Image.open(img_path).convert("L")
            ( width, height ) = pil.size
            raw = pil.tobytes()
            zbar_image = zbar.Image(width, height, "Y800", raw)
            return self.decode(zbar_image)

        except IOError:
            print "IOError"
            return None

    def decode_bytes(self, width, height, fourcc, bytes_object):
        zbar_image = zbar.Image(width, height, fourcc, bytes_object)
        return self.decode(zbar_image)
        
    def decode(self, zbar_image):
        self.scanner.scan(zbar_image)
        for symbol in zbar_image:
            print "decoded", symbol.type, "symbol", '"%s"' % symbol.data
            return symbol.data
        return None