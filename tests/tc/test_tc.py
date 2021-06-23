import unittest
from tc import Tc

class TestTc(unittest.TestCase):
    def test_units(self):
        tc_string = '0:12:12f'
        tc_tc = Tc(tc_string, 25)
        result = tc_tc._units
        expected = 'smpte'
        self.assertEqual(result, expected)

    def test_fr(self):
        tc_string = '0:12:12f'
        tc_tc = Tc(tc_string, 25)
        result = tc_tc._fr
        expected = 25
        self.assertEqual(result, expected)

    def test_hmsf(self):
        tc_string = '0:12:12f'
        tc_tc = Tc(tc_string, 25)
        result_hmsf = tc_tc.hmsf
        expected_hmsf = '00:00:12:12'
        self.assertEqual(result_hmsf, expected_hmsf)

    def test_seconds(self):
        tc_string = '0:12:12f'
        tc_tc = Tc(tc_string, 25)
        result = tc_tc._seconds
        expected = 12.48
        self.assertEqual(result, expected)

    def test_frames(self):
        tc_string = '0:12:12f'
        tc_tc = Tc(tc_string, 25)
        result = tc_tc._frames
        expected = 312
        self.assertEqual(result, expected)

    def test_hmsf_setter(self):
        tc_string = '0:12:12f'
        tc_tc = Tc(tc_string, 25)
        new_tc_string = '0:13:13f'
        tc_tc.hmsf = new_tc_string

        result_hmsf = tc_tc.hmsf
        expected_hmsf = '00:00:13:13'
        self.assertEqual(result_hmsf, expected_hmsf)

        result_seconds = tc_tc._seconds
        expected_seconds = 13.52
        self.assertEqual(result_seconds, expected_seconds)

        result_frames = tc_tc._frames
        expected_frames = 338
        self.assertEqual(result_frames, expected_frames)

    def test_mutate_smpte_hms(self):
        tc_string = '0:12:12f'
        tc_tc = Tc(tc_string, 25)
        tc_tc.mutate()
        result_hmsf = tc_tc.hmsf
        expected_hmsf = '00:00:12.480'
        self.assertEqual(result_hmsf, expected_hmsf)

    def test_mutate_hms_smpte(self):
        tc_string = '0:12:12.48'
        tc_tc = Tc(tc_string)
        tc_tc.mutate(25)
        result_hmsf = tc_tc.hmsf
        expected_hmsf = '00:12:12:12'
        self.assertEqual(result_hmsf, expected_hmsf)

if __name__ == '__main__':
    unittest.main()




