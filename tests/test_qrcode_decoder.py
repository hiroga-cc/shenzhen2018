import os, sys, unittest
from PIL import Image
sys.path.append("src/")
from qrcode_decoder import QrcodeDecoder

class QrcodeDecoderTest(unittest.TestCase):
    def test_1234567890(self):
        r = QrcodeDecoder()
        expected = "1234567890"
        actual = r.decode_file("tests/test_qrcode/1234567890.png")
        self.assertEqual(expected, actual)

    def test_1234567890_r(self):
        r = QrcodeDecoder()
        expected = "1234567890"
        actual = r.decode_file("tests/test_qrcode/1234567890_r.png")
        self.assertEqual(expected, actual)

    def test_btc(self):
        r = QrcodeDecoder()
        actual = r.decode_file("tests/test_qrcode/btc.jpg")
        self.assertIsNotNone(actual)

    def test_not_qrcode(self):
        r = QrcodeDecoder()
        expected = None
        actual = r.decode_file("tests/test_qrcode/cat.jpg")
        self.assertEqual(expected, actual)

    def test_nofile(self):
        r = QrcodeDecoder()
        expected = None
        actual = r.decode_file("nofile")
        self.assertEqual(expected, actual)

    def test_wrong_type(self):
        r = QrcodeDecoder()
        expected = None
        actual = r.decode_file(None)
        self.assertEqual(expected, actual)

    def test_from_bytes(self):
        r = QrcodeDecoder()
        bytes_object = Image.open("tests/test_qrcode/1234567890.png").convert("L").tobytes()
        expected = "1234567890"
        actual = r.decode_bytes(200, 200, "Y800", bytes_object)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()