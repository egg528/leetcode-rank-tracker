# -*- coding: utf-8 -*-

from .context import tracker

import unittest


class AdvancedTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_thoughts(self):
        self.assertIsNone(tracker.hmm())


if __name__ == '__main__':
    unittest.main()
