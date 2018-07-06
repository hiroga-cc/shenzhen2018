import os, sys, unittest
from PIL import Image
sys.path.append("src/")
from qrcode_reader import QrcodeReader

class QrcodeReaderTest(unittest.TestCase):
    def test(self):
        r = QrcodeReader()
        actual = r.capture_once()
        self.assertIsNotNone(actual)