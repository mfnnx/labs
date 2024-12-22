from lab_python_oop.figure import Figure
from lab_python_oop.color import Color

class Rectangle(Figure):
    FIGURE_TYPE = "Прямоугольник"

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = Color(color)

    def area(self):
        return self.width * self.height

    @classmethod
    def name(cls):
        return cls.FIGURE_TYPE

    def __repr__(self):
        return "Фигура: {}, цвет: {}, ширина: {}, высота: {}, площадь: {:.2f}".format(
            self.name(), self.color.color, self.width, self.height, self.area()
        )
