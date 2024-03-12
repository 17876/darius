import unittest
from darius.dash import Container, Dash
from darius.tc import Tc

class TestDash(unittest.TestCase):
    def test_init(self):
        cont_1 = Container('test', [1, 2, 3])
        cont_1.data = [5, 6, 7]

    def test_getitem_1(self):
        cont_1 = Container('test', [1, 2, 3])
        result = cont_1[1]
        expected = 2
        self.assertEqual(result, expected)

    def test_getitem_2(self):
        start_1 = Tc('0:0:0', 'hms')
        end_1 = Tc('0:1:12.56', 'hms')
        dash_1 = Dash('Dash_1', start_1, end_1)

        start_2 = Tc('0:1:13.56', 'hms')
        end_2 = Tc('0:1:15.56', 'hms')
        dash_2 = Dash('Dash_2', start_2, end_2)

        cont_1 = Container('test', [dash_1, dash_2])

        result = cont_1['Dash_2']

        # print(result)


if __name__ == '__main__':
    unittest.main()




