#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import time
from servo import ServoClass

class unit_tests_servo(unittest.TestCase):

    def __init__(self, *args):
        super(unit_tests_servo, self).__init__(*args)
        self.servo = ServoClass(0)
        self.servob = ServoClass(1)

    def test_servo(self):
        '''
            Tries servo by rotating randomly
        '''
        for i in range(300):
            self.servo.go_circle((i+45)*6, 0)
            self.servob.go_circle((i+45)*6, 1)
            time.sleep(0.01)
        self.assertTrue(self.servo.angle <= self.servo._ServoClass__max_value)
        self.assertTrue(self.servo.angle >= self.servo._ServoClass__min_value)
        self.servo.angle_reset()
        self.servob.angle_reset()

if __name__ == '__main__':
    unittest.main(buffer=True, verbosity=2)
