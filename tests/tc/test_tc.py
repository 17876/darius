import unittest
from darius.tc import Tc

class TestTc(unittest.TestCase):
    def test_units1(self):
        timecode = '0:12:12'
        units = 'hms'
        tc_tc = Tc(timecode, units, 25)
        result = tc_tc.units
        expected = 'hms'
        self.assertEqual(result, expected)

    def test_units2(self):
        timecode = '0:12:12'
        units = 'hms'
        tc_tc = Tc(timecode, units)
        result = tc_tc.units
        expected = 'hms'
        self.assertEqual(result, expected)

    def test_seconds1(self):
        timecode = '0:12:12'
        units = 'smpte'
        tc_tc = Tc(timecode, units, 25)
        result = tc_tc.seconds
        expected = 12.48
        self.assertEqual(result, expected)

    def test_seconds2(self):
        timecode = '0:01:12.654'
        units = 'hms'
        tc_tc = Tc(timecode, units)
        result = tc_tc.seconds
        expected = 72.654
        self.assertEqual(result, expected)

    def test_fr(self):
        timecode = '0:12:12'
        units = 'smpte'
        tc_tc = Tc(timecode, units, 25)
        result = tc_tc.fr
        expected = 25
        self.assertEqual(result, expected)

    def test_timecode(self):
        timecode = '0:12:12'
        units = 'smpte'
        tc_tc = Tc(timecode, units, 25)
        result_timecode = tc_tc.timecode
        expected_timecode = '00:00:12:12'
        self.assertEqual(result_timecode, expected_timecode)

    def test_frames(self):
        timecode = '0:12:12'
        units = 'smpte'
        tc_tc = Tc(timecode, units, 25)
        result = tc_tc.frames
        expected = 312
        self.assertEqual(result, expected)

    def test_timecode_setter(self):
        timecode = '0:12:12'
        units = 'smpte'
        tc_tc = Tc(timecode, units, 25)
        new_tc_string = '0:13:13'
        tc_tc.timecode = new_tc_string

        result_timecode = tc_tc.timecode
        expected_timecode = '00:00:13:13'
        self.assertEqual(result_timecode, expected_timecode)

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
        self.assertEqual(result, expected)

    def test_add_2(self):
        hmsf_human_1 = '0:1:12'
        hmsf_human_2 = '0:1:13'
        units = 'smpte'
        tc_1 = Tc(hmsf_human_1, units, 25)
        tc_2 = Tc(hmsf_human_2, units, 25)
        result = tc_1 + tc_2
        expected = Tc('0:3:0', units, 25)
        self.assertEqual(result, expected)

    def test_multiply(self):
        timecode = '0:1:12'
        number = 2.5
        units = 'hms'
        tc = Tc(timecode, units)
        result = tc * number
        expected = Tc('0:3:00', units)
        # print(result)
        self.assertEqual(result, expected)

    def test_sub(self):
        tc_human_1 = '0:1:12'
        tc_human_2 = '0:1:11'
        units = 'hms'
        tc_1 = Tc(tc_human_1, units)
        tc_2 = Tc(tc_human_2, units)
        result = tc_1 - tc_2
        # print(result)
        expected = Tc('0:0:1', units)
        self.assertEqual(result, expected)

    def test_div1(self):
        tc_human = '0:1:12'
        num = 2
        units = 'hms'
        tc = Tc(tc_human, units)
        result = tc / num
        expected = Tc('0:0:36', units)
        # print(result)
        self.assertEqual(result, expected)

    def test_div2(self):
        tc_human1 = '0:1:12'
        tc_human2 = '0:0:36'
        units = 'hms'
        tc1 = Tc(tc_human1, units)
        tc2 = Tc(tc_human2, units)
        result = tc1 / tc2
        expected = 2
        # print(result)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()




