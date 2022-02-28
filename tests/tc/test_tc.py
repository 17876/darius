import unittest
from darius.tc import Tc

class TestTc(unittest.TestCase):
    def test_units(self):
        hmsf_human = '0:12:12'
        units = 'smpte'
        tc_tc = Tc(hmsf_human, units, 25)
        result = tc_tc.units
        expected = 'smpte'
        self.assertEqual(result, expected)

    def test_seconds(self):
        hmsf_human = '0:12:12'
        units = 'smpte'
        tc_tc = Tc(hmsf_human, units, 25)
        result = tc_tc.seconds
        expected = 12.48
        self.assertEqual(result, expected)

    def test_fr(self):
        hmsf_human = '0:12:12'
        units = 'smpte'
        tc_tc = Tc(hmsf_human, units, 25)
        result = tc_tc.fr
        expected = 25
        self.assertEqual(result, expected)

    def test_hmsf(self):
        hmsf_human = '0:12:12'
        units = 'smpte'
        tc_tc = Tc(hmsf_human, units, 25)
        result_hmsf = tc_tc.hmsf
        expected_hmsf = '00:00:12:12'
        self.assertEqual(result_hmsf, expected_hmsf)

    def test_frames(self):
        hmsf_human = '0:12:12'
        units = 'smpte'
        tc_tc = Tc(hmsf_human, units, 25)
        result = tc_tc.frames
        expected = 312
        self.assertEqual(result, expected)

    def test_hmsf_setter(self):
        hmsf_human = '0:12:12'
        units = 'smpte'
        tc_tc = Tc(hmsf_human, units, 25)
        new_tc_string = '0:13:13'
        tc_tc.hmsf = new_tc_string

        result_hmsf = tc_tc.hmsf
        expected_hmsf = '00:00:13:13'
        self.assertEqual(result_hmsf, expected_hmsf)

        result_seconds = tc_tc.seconds
        expected_seconds = 13.52
        self.assertEqual(result_seconds, expected_seconds)

        result_frames = tc_tc.frames
        expected_frames = 338
        self.assertEqual(result_frames, expected_frames)

    def test_eq_1(self):
        hmsf_human_1 = '0:1:12'
        hmsf_human_2 = '0:1:12'
        units = 'smpte'
        tc_1 = Tc(hmsf_human_1, units, 25)
        tc_2 = Tc(hmsf_human_2, units, 25)
        result = (tc_1 == tc_2)
        expected = True
        self.assertEqual(result, expected)

    def test_eq_2(self):
        hmsf_human_1 = '0:1:12'
        hmsf_human_2 = '0:1:2'
        units = 'smpte'
        tc_1 = Tc(hmsf_human_1, units, 25)
        tc_2 = Tc(hmsf_human_2, units, 25)
        result = (tc_1 == tc_2)
        expected = False
        self.assertEqual(result, expected)


    def test_add_1(self):
        hmsf_human_1 = '0:1:12'
        hmsf_human_2 = '0:1:11'
        units = 'smpte'
        tc_1 = Tc(hmsf_human_1, units, 25)
        tc_2 = Tc(hmsf_human_2, units, 25)
        result = tc_1 + tc_2
        expected = Tc('0:2:23', units, 25)
        print(result)
        self.assertEqual(result, expected)

    def test_add_2(self):
        hmsf_human_1 = '0:1:12'
        hmsf_human_2 = '0:1:13'
        units = 'smpte'
        tc_1 = Tc(hmsf_human_1, units, 25)
        tc_2 = Tc(hmsf_human_2, units, 25)
        result = tc_1 + tc_2
        expected = Tc('0:3:0', units, 25)
        print(result)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()




