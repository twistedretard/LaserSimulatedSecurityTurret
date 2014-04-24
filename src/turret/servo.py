#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import sys
import math

class ServoClass(object):
    '''
        Representer of a servo connected at pin "pin"
    '''
    def save_decorator(f):
        def inner_func(self, *args, **kw):
            try:
                return f(self, *args, **kw)
            finally:
                self.do_save()
        return inner_func

    def __init__(self, pin=None):
        self.__max_value = 200
        self.__min_value = 60
        self.__start_value = 140
        self.__servo_file = '/dev/servoblaster'
        self.angle = self.__start_value
        if pin < 0 or pin > 7:
            raise
        self.pin = pin
        self.do_save()

    def __str__(self):
        return "Servo nr: {0}, Angle: {1}".format(self.pin, self.angle)

    def reset(self):
        self.angle = self.__start_value
        self.do_save()

    @save_decorator
    def turn_left(self):
        '''
            Reduces the angle of the servo by 1
        '''
        self.angle = max(self.angle - 1, self.__min_value)

    @save_decorator
    def turn_right(self):
        '''
            Increases the angle of servo by 1
        '''
        self.angle = min(self.angle + 1, self.__max_value)

    @save_decorator
    def go_random(self):
        '''
            Positions the servo to a random position between the min and max values.
            Mosly used for demoing purpose.
        '''
        minrandom = self.angle-30
        maxrandom = self.angle+30
        if minrandom < self.__min_value:
            maxrandom += self.__min_value - minrandom
            minrandom = self.__min_value
        if maxrandom > self.__max_value:
            minrandom += self.__max_value - maxrandom
            maxrandom = self.__max_value
            
        self.angle = random.randint(minrandom, maxrandom)
        #self.angle = random.randint(self.angle-40 if self.angle-40 >= self.__min_value, self.angle+40 if self.angle+40 <= self.__max_value)
    
    @save_decorator
    def go_circle(self, angle, servo):
        '''
            Positions the servo to the specified angle.
        '''
        if servo == 0:
            self.angle = int(30*math.sin(math.radians(angle)) + self.__min_value + (self.__max_value / 2))
        else:
            self.angle = int(50*math.cos(math.radians(angle)) + self.__min_value + (self.__max_value / 2) - 15)

    def do_save(self):
        '''
            Writes the angle to the file used by servoblaster kernel module
        '''
        if sys.flags.debug:
            sys.stderr.write('{0}={1}\n'.format(self.pin, self.angle))
        else:
            with open(self.__servo_file, 'w') as sblaster:
                sblaster.write('{0}={1}\n'.format(self.pin, self.angle))
