import sys
import os

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir)


import rectangle
import unittest

class RectangleTestCase(unittest.TestCase):
    def test_zero_multiple(self):
        res1 = rectangle.area(0, 123)
        res2 = rectangle.perimeter(0, 0)
        self.assertEqual(res1, 0)
        self.assertEqual(res2, 0)
    
    def test_float_numbers(self):
        res1 = rectangle.area(3.7, 10.1)
        res2 = rectangle.perimeter(23.7, 19)
        self.assertEqual(res1, 37.37)
        self.assertEqual(res2, 85.4)

    def test_diffirent_numbers(self):
        res1 = rectangle.area(4, 5)
        res2 = rectangle.perimeter(4, 5)
        self.assertEqual(res1, 20)
        self.assertEqual(res2, 18)
    
    def test_big_numbers(self):
        res1 = rectangle.area(10000003332, 100000000)
        res2 = rectangle.perimeter(1232900, 100000000)
        self.assertEqual(res1, 1000000333200000000)
        self.assertEqual(res2, 202465800)

if __name__ == '__main__':
    unittest.main()