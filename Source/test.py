import unittest
import turret

class IsOddTests(unittest.TestCase):

    def testOne(self):
        angle = turret.get_angle()
        turret.turn_right()
        self.assertTrue(turret.get_angle() > angle)
def main():
    unittest.main()

if __name__ == '__main__':
    main()