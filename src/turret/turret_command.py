from enum import Enum

class TurretCommand(object):

    class ServoState(Enum):
        off = 0
        inc = 1
        dec = 2
        reset = 3
    class LaserState(Enum):
        off = 0
        on = 1
    class ExtraState(Enum):
        off = 0
        camera = 1

    def __init__(self, value=0):
        if isinstance(value, bytes):
            self.__value = int.from_bytes(value, byteorder='little')
        else:
            self.__value = value

    def __int__(self):
        return self.__value & 0xff

    def __str__(self):
        return ('Servo X: ' + str(self.servo_x) + '\n'
                'Servo Y: ' + str(self.servo_y) + '\n'
                'Laser:   ' + str(self.laser) + '\n')

    def __repr__(self):
        return str(self.__value)

    def __call__(self, value):
        if isinstance(value, bytes):
            self.__value = int.from_bytes(value, byteorder='little')
        else:
            self.__value = value

    def __bytes__(self):
        return self.__value.to_bytes(1, byteorder='little')

    #Descriptors for everything!!!
    #A quote stemming from Socrates explains why: Because i was bored!
    def __getx(self):
        return (self.__value & 0xc0) >> 6
    def __setx(self, value):
        try:
            value = value.value
        except:
            pass
        self.__value = (self.__value & (255 ^ 0xc0) | ((value & 3) << 6))
    servo_x = property(__getx, __setx, None, '')

    def __gety(self):
        return (self.__value & 0x30) >> 4
    def __sety(self, value):
        try:
            value = value.value
        except:
            pass
        self.__value = (self.__value & (255 ^ 0x30) | (((value &  3)) << 4))
    servo_y = property(__gety, __sety, None, '')

    def __getlaser(self):
        return (self.__value & 0x8) >> 3
    def __setlaser(self, value):
        try:
            value = value.value
        except:
            pass
        self.__value = (self.__value & (255 ^ 0x8) | ((value & 1) << 3))
    laser = property(__getlaser, __setlaser, None, '')

    def __getextra(self):
        return self.__value & 7
    def __setextra(self, value):
        try:
            value = value.value
        except:
            pass
        self.__value = (self.__value & (255 ^ 7) | (value & 7))
    extra = property(__getextra, __setextra, None, '')

    encode = lambda x: x.to_bytes(1, byteorder='little')
    decode = lambda x: int.from_bytes(x, byteorder='little')

    def value(self):
        return self.__value
