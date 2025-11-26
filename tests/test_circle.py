import sys
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import circle
import unittest

class CircleTestCase(unittest.TestCase):
    def test_zero_multiple(self):
        res1 = circle.area(0)
        res2 = circle.perimeter(0)
        self.assertEqual(res1, 0)
        self.assertEqual(res2, 0)
    
    def test_calculation(self):
        res1 = circle.area(52)
        res2 = circle.perimeter(17)
        self.assertEqual(res1, 8494.8665353068)
        self.assertEqual(res2, 106.81415022205297)
    
    def test_float_numbers(self):
        res1 = circle.area(50.9)
        res2 = circle.perimeter(15.1)
        self.assertEqual(res1, 8139.269662846972)
        self.assertEqual(res2, 94.87609813841175)
    
    def test_big_numbers(self):
        res1 = circle.area(999888999888)
        res2 = circle.perimeter(10070)
        self.assertEqual(res1, 3.140895258024621e+24)
        self.assertEqual(res2, 63271.67604329843)

if __name__ == '__main__':
    unittest.main()