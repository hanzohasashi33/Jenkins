#!/usr/bin/env python

import unittest
import logging

from main import divisible

formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')


def setup_logger(name, log_file, level=logging.INFO):
    handler = logging.FileHandler(log_file)        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


# first file logger
logger = setup_logger('first_logger', 'logfile.log')
logger.info('This is just info message')


class TestSort(unittest.TestCase):
    def test_divisible(self):
        logger.info("Testing divisible")
        self.assertTrue(divisible(4,2))

    def test_notdivisible(self):
        logger.info("Testing not divisible")
        self.assertEqual(divisible(4,3), False)

    def test_divisiblebyzero(self):
        logger.info("Testing divisible by zero - division should not be permitted")
        self.assertEqual(divisible(4,0), "Division by zero not permitted")



if  __name__ == '__main__':
    logger.info("Running unit tests")
    unittest.main()
    logger.info("Unit tests complete")