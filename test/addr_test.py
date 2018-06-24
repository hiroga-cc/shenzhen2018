import os, sys, unittest
sys.path.append("../src/")
from addr import AddrHandler

ADDRESS = "1QEnd3LMAtjUbo2WfL6xHGmc8TGQZvgKpg"

class AddrTest(unittest.TestCase):
    def test_cut_addr(self):
        # make file
        h = AddrHandler()
        expected = ADDRESS 
        actual = h.cut_addr()
        self.assertEqual(expected, actual)
        self.assertEqual("", h.read_addr())
    
    def test_cut_blank_addr(self):
        # file clean
        h = AddrHandler()
        expected = ""
        actual = h.cut_addr()
        self.assertEqual(expected, actual)

    def test_write_addr(self):
        h = AddrHandler()
        expected = ADDRESS
        h.write_addr(ADDRESS)
        actual = h.read_addr()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    print("unittest start")
    unittest.main()
