import unittest
from darius.dash import Dash
from darius.tc import Tc

class TestDash(unittest.TestCase):
    def test_init(self):
        start = Tc('0:0:0', 'hms')
        end = Tc('0:1:12.56', 'hms')
        dash = Dash('TestInit', start, end)
        # print(dash)

    def test_dur1(self):
        start = Tc('0:0:2', 'hms')
        end = Tc('0:1:12.56', 'hms')
        dash = Dash('TestInit', start, end)
        # print(dash)

    def test_dur2(self):
        start = Tc('0:0:2', 'hms')
        end = Tc('0:1:12.56', 'hms')
        dash = Dash('TestInit', start, end)
        dash.end = Tc('0:1:13.56', 'hms')
        # print(dash)

    def test_dur3(self):
        start = Tc('0:0:2', 'hms')
        end = Tc('0:1:12.56', 'hms')
        dash = Dash('TestInit', start, end)
        dash.dur = Tc('0:2:0', 'hms')
        # print(dash)

    def test_dur4(self):
        start = Tc('0:0:2', 'hms')
        end = Tc('0:1:12.56', 'hms')
        dash = Dash('TestInit', start, end)
        dash.start = Tc('0:0:5', 'hms')
        # print(dash)




if __name__ == '__main__':
    unittest.main()




