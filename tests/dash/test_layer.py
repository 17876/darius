import unittest
from darius.dash import Dash, Layer
from darius.tc import Tc

class TestLayer(unittest.TestCase):
    def test_init(self):
        start_1 = Tc('0:0:0', 'hms')
        end_1 = Tc('0:0:10.56', 'hms')
        dash_1 = Dash('TestInit', start_1, end_1)

        start_2 = Tc('0:0:11', 'hms')
        end_2 = Tc('0:0:12.56', 'hms')
        dash_2 = Dash('TestInit', start_2, end_2)
        # print(dash)

        layer_1 = Layer('Layer TestInit', [dash_1, dash_2])

        print(layer_1)





if __name__ == '__main__':
    unittest.main()




