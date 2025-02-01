#Ryan Feroz 
#SSW567 HW00b

import unittest
from triangle import classify_triangle  #Imports function from triangle.py

class TestClassifyTriangle(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(classify_triangle(5, 5, 5), "Equilateral")

    def test_isosceles(self):
        self.assertEqual(classify_triangle(5, 5, 3), "Isosceles")

    def test_scalene(self):
        self.assertEqual(classify_triangle(4, 5, 6), "Scalene")

    def test_right_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene Right")

    def test_invalid_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Invalid Triangle")

if __name__ == "__main__":
    unittest.main()