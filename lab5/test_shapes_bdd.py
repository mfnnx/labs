from pytest_bdd import scenarios, given, then
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

# Подключение файла feature
scenarios('features/shapes.feature')

# Шаги

@given("I have a rectangle with width 4 and height 5")
def rectangle():
    return Rectangle(4, 5, "синий")

@then("the area of the rectangle should be 20")
def check_rectangle_area(rectangle):
    assert rectangle.area() == 20

@given("I have a circle with radius 3")
def circle():
    return Circle(3, "зеленый")

@then("the area of the circle should be approximately 28.27")
def check_circle_area(circle):
    assert round(circle.area(), 2) == 28.27

@given("I have a square with side 4")
def square():
    return Square(4, "красный")

@then("the area of the square should be 16")
def check_square_area(square):
    assert square.area() == 16
