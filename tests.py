#!/usr/bin/env python

import unittest
from unittest.main import main

from main import divisible

class TestSort(unittest.TestCase):
    def test_divisible(self):
        self.assertTrue(divisible(4,2))

    def test_notdivisible(self):
        self.assertEqual(divisible(4,3), False)



if  __name__ == '__main__':
    unittest.main()