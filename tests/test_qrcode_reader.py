import os, sys, unittest
sys.path.append("src/")
from qrcode_reader import QrcodeReader

class QrcodeReaderTest(unittest.TestCase):
    def test(self):
        r = QrcodeReader()
        actual = r.capture_once()
        self.assertIsNotNone(actual)