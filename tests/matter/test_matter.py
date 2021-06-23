import unittest
from matter import MatterDatabase

class TestMatter(unittest.TestCase):
    def test_1(self):
        db = MatterDatabase('test_materia.json', 'Videos')
        print(db)

if __name__ == '__main__':
    unittest.main()
