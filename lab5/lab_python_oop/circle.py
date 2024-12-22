from lab_python_oop.figure import Figure
from lab_python_oop.color import Color
import math

class Circle(Figure):
    FIGURE_TYPE = "Круг"

    def __init__(self, radius, color):
        self.radius = radius
        self.color = Color(color)

    def area(self):
        return math.pi * (self.radius ** 2)

    @classmethod
    def name(cls):
        return cls.FIGURE_TYPE

    def __repr__(self):
        return "Фигура: {}, цвет: {}, радиус: {}, площадь: {:.2f}".format(
            self.name(), self.color.color, self.radius, self.area()
        )
