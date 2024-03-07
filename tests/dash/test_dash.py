import unittest
from darius.dash import Dash
from darius.tc import Tc

class TestDash(unittest.TestCase):
    def test_init(self):
        start = Tc('0:0:0', 'hms')
        end = Tc('0:1:12.56', 'hms')
        dash = Dash('TestInit', start, end)
        print(dash)




if __name__ == '__main__':
    unittest.main()




