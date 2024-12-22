import unittest
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
from main import create_shapes, use_numpy_example

class TestShapes(unittest.TestCase):

    def test_rectangle_area(self):
        """Тест площади прямоугольника"""
        rect = Rectangle(4, 5, "синий")
        self.assertEqual(rect.area(), 20, "Площадь прямоугольника должна быть 20")

    def test_circle_area(self):
        """Тест площади круга"""
        circle = Circle(3, "зеленый")
        self.assertAlmostEqual(circle.area(), 28.27, places=2, msg="Площадь круга должна быть примерно 28.27")

    def test_square_area(self):
        """Тест площади квадрата"""
        square = Square(4, "красный")
        self.assertEqual(square.area(), 16, "Площадь квадрата должна быть 16")

class TestNumpyExample(unittest.TestCase):

    def test_numpy_sum(self):
        """Тест функции использования numpy"""
        result = use_numpy_example()
        self.assertEqual(result, 15, "Сумма элементов массива должна быть 15")

if __name__ == "__main__":
    unittest.main()
