import unittest
from lib.shapes import Circle, Triangle


class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), 78.5398163397)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0)

    def test_triangle_right(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right())

    def test_triangle_not_right(self):
        triangle = Triangle(3, 4, 6)
        self.assertFalse(triangle.is_right())


if __name__ == '__main__':
    unittest.main()
