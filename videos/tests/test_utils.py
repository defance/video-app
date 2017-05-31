from __future__ import unicode_literals

import unittest

from django.utils import translation
from django.utils.translation import pgettext as _p, ugettext as _u

from ..utils import (extract_raw_duration_info, extract_duration_info,
                     get_duration_str)


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


class TestGetDurationStr(unittest.TestCase):

    def test_str_correct(self):
        case = {'h': 1, 'm': 2, 's': 3.45}
        expected = " ".join([
            '1', _p('duration', 'hrs'),
            '2', _p('duration', 'min'),
            '3.45', _p('duration', 'sec')
        ])
        self.assertEqual(expected, get_duration_str(case))

    def test_something_missing(self):
        case = {'s': 1.23}
        expected = " ".join([
            '1.23', _p('duration', 'sec')
        ])
        self.assertEqual(expected, get_duration_str(case))

    def test_something_zero(self):
        case = {'h': 0, 'm': 0, 's': 1.23}
        expected = " ".join([
            '1.23', _p('duration', 'sec')
        ])
        self.assertEqual(expected, get_duration_str(case))

    def test_all_zero(self):
        case = {'h': 0, 'm': 0, 's': 0}
        expected = _u('Unknown')
        self.assertEqual(expected, get_duration_str(case))

    def test_all_missing(self):
        case = {}
        expected = _u('Unknown')
        self.assertEqual(expected, get_duration_str(case))

    def test_str_correct_long(self):
        # seconds will be rounded
        seconds = 123.4567890
        case = {'h': 123, 'm': 456, 's': seconds}
        expected = " ".join([
            '123', _p('duration', 'hrs'),
            '456', _p('duration', 'min'),
            '{:.2f}'.format(seconds), _p('duration', 'sec')
        ])
        self.assertEqual(expected, get_duration_str(case))

    def test_str_correct_with_noise(self):
        case = {'h': 1, 'm': 2, 's': 3.45, 'noise': 'foo'}
        expected = " ".join([
            '1', _p('duration', 'hrs'),
            '2', _p('duration', 'min'),
            '3.45', _p('duration', 'sec')
        ])
        self.assertEqual(expected, get_duration_str(case))

    def test_str_only_noise(self):
        case = {'noise': 'foo'}
        expected = _u('Unknown')
        self.assertEqual(expected, get_duration_str(case))
