from __future__ import unicode_literals

import unittest

from ..utils import extract_raw_duration_info, extract_duration_info


class TestExtractRawDurationInfo(unittest.TestCase):

    def test_has_duration(self):
        s = 'duration=01:23:45.67890'
        self.assertEqual(extract_raw_duration_info(s), '01:23:45.67890')

    def test_duration_malformed(self):
        s = 'duration=1234567890'
        self.assertEqual(extract_raw_duration_info(s), None)

    def test_duration_empty(self):
        s = 'duration='
        self.assertEqual(extract_raw_duration_info(s), None)

    def test_duration_with_noise(self):
        s = 'noise\nduration=01:23:45.67890\nnoise'
        self.assertEqual(extract_raw_duration_info(s), '01:23:45.67890')


class TestExtractDurationInfo(unittest.TestCase):

    def test_duration_correct(self):
        case = '01:23:45.678900'
        expected = {
            'h': float(01),
            'm': float(23),
            's': float(45.678900)
        }
        self.assertDictEqual(expected, extract_duration_info(case))

    def test_duration_zeros(self):
        case = '00:00:00.00000'
        expected = {
            'h': float(0),
            'm': float(0),
            's': float(0)
        }
        self.assertDictEqual(expected, extract_duration_info(case))

    def test_duration_malformed(self):
        case = 'not_matching_expression'
        self.assertDictEqual({}, extract_duration_info(case))

    def test_duration_misc_length(self):
        case = '1234567890:1:2.3'
        expected = {
            'h': float(1234567890),
            'm': float(1),
            's': float(2.3)
        }
        self.assertDictEqual(expected, extract_duration_info(case))
