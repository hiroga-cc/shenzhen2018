import os, sys, unittest
sys.path.append("src/")
from addr_validator import *

DECORATED_ADDR = "bitcoin:1HER2wsB1vro42YhVQRu8YjPVHPbFMfCVt?amount=0"
ADDRESS = "1HER2wsB1vro42YhVQRu8YjPVHPbFMfCVt"

class AddrTest(unittest.TestCase):
    def test_trim_addr(self):
        expected = ADDRESS
        actual = trim_addr(DECORATED_ADDR)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()