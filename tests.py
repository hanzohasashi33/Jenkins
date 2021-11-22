#!/usr/bin/env python

import unittest

from main import divisible

class TestSort(unittest.TestCase):
    def test_divisible(self):
        self.assertTrue(divisible(4,2))

    def test_notdivisible(self):
        self.assertEqual(divisible(4,3), False)

    def test_divisiblebyzero(self):
        self.assertEqual(divisible(4,0), "Division by zero not permitted")



if  __name__ == '__main__':
    unittest.main()