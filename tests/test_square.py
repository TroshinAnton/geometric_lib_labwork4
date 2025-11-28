import sys
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import square
import unittest

class SquareTestCase(unittest.TestCase):
    def test_zero_multiple(self):
        res1 = square.area(0)
        res2 = square.perimeter(0)
        self.assertEqual(res1, 0)
        self.assertEqual(res2, 0)
    
    def test_calculation(self):
        res1 = square.area(52)
        res2 = square.perimeter(17)
        self.assertEqual(res1, 2704)
        self.assertEqual(res2, 68)
    
    def test_float_numbers(self):
        res1 = square.area(57.9)
        res2 = square.perimeter(15.1)
        self.assertEqual(res1, 3352.41)
        self.assertEqual(res2, 60.4)
    
    def test_big_numbers(self):
        res1 = square.area(9998889888)
        res2 = square.perimeter(10070)
        self.assertEqual(res1, 99977798992348652544)
        self.assertEqual(res2, 40280)

if __name__ == '__main__':
    unittest.main()