import unittest
from darius.matter import Marker
from darius.tc import Tc

class TestMarker(unittest.TestCase):
    def test_1(self):
        start_string = '0:25:12f'
        end_string = '0:29:13f'
        start_tc = Tc(start_string, 25)
        end_tc = Tc(end_string, 25)
        ma = Marker('Marker_01', start_tc, end_tc)
        print(ma)

if __name__ == '__main__':
    unittest.main()
