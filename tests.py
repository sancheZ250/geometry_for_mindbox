import unittest
from shapes import Circle, Triangle
from utils import calculate_area


class TestShapes(unittest.TestCase):
    def test_circle_area(self):
        circle = Circle(3)
        self.assertAlmostEqual(circle.area(), 28.274333882308138)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6.0)

    def test_triangle_is_right(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_triangle())

        triangle = Triangle(5, 5, 5)
        self.assertFalse(triangle.is_right_triangle())

    def test_calculate_area_circle(self):
        circle = Circle(3)
        self.assertAlmostEqual(calculate_area(circle), 28.274333882308138)

    def test_calculate_area_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(calculate_area(triangle), 6.0)

    def test_invalid_shape(self):
        with self.assertRaises(TypeError):
            calculate_area("not a shape")


if __name__ == "__main__":
    unittest.main()
