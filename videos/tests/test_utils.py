from __future__ import unicode_literals

import unittest

from ..utils import extract_raw_duration_info


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
