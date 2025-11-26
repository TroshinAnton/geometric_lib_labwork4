import sys
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)

import triangle
import unittest

class TriangleTestCase(unittest.TestCase):
    def test_zero_multiple(self):
        res1 = triangle.area(0, 0)
        res2 = triangle.perimeter(0, 0, 0)
        self.assertEqual(res1, 0)
        self.assertEqual(res2, 0)
    
    def test_calculation(self):
        res1 = triangle.area(4, 2)
        res2 = triangle.perimeter(4, 2, 4)
        self.assertEqual(res1, 4)
        self.assertEqual(res2, 10)

    def test_float_numbers(self):
        res1 = triangle.area(4.5, 2)
        res2 = triangle.perimeter(4, 2.1, 4)
        self.assertEqual(res1, 4.5)
        self.assertEqual(res2, 10.1)
    
    def test_big_numbers(self):
        res1 = triangle.area(10000000000, 200)
        res2 = triangle.perimeter(100, 1000000000, 100000000000000000)
        self.assertEqual(res1, 1000000000000)
        self.assertEqual(res2, 100000001000000100)