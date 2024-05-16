import unittest
from laba3 import Circle, Square, Red, Blue, Rectangle, Green

class TestShapes(unittest.TestCase):
    def test_red_circle_draw(self):
        red_circle = Circle(Red())
        self.assertEqual(red_circle.draw(), "Drawing a red circle.")

    def test_blue_square_draw(self):
        blue_square = Square(Blue())
        self.assertEqual(blue_square.draw(), "Drawing a blue square.")

    def test_green_rectangle_draw(self):
        green_rectangle = Rectangle(Green())
        self.assertEqual(green_rectangle.draw(), "Drawing a green rectangle.")   

    def test_red_square_draw(self):
        red_square = Square(Red())
        self.assertEqual(red_square.draw(), "Drawing a red square.")

    def test_red_rectangle_draw(self):
        red_rectangle = Rectangle(Red())
        self.assertEqual(red_rectangle.draw(), "Drawing a red rectangle.")

    def test_blue_circle_draw(self):
        blue_circle = Circle(Blue())
        self.assertEqual(blue_circle.draw(), "Drawing a blue circle.")

    def test_blue_rectangle_draw(self):
        blue_rectangle = Rectangle(Blue())
        self.assertEqual(blue_rectangle.draw(), "Drawing a blue rectangle.")

    def test_green_circle_draw(self):
        green_circle = Circle(Green())
        self.assertEqual(green_circle.draw(), "Drawing a green circle.")

    def test_green_square_draw(self):
        green_square = Square(Green())
        self.assertEqual(green_square.draw(), "Drawing a green square.")

if __name__ == "__main__":
    unittest.main()
