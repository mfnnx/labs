from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import numpy as np


def create_shapes(n):

   # Создает три объекта: прямоугольник, круг и квадрат.

    rect = Rectangle(n, n, "синий")
    circle = Circle(n, "зеленый")
    square = Square(n, "красный")
    return rect, circle, square


def use_numpy_example():

    # Пример использования numpy: сумма элементов массива.

    arr = np.array([1, 2, 3, 4, 5])
    return np.sum(arr)


def main():
    n = 22
    # Создание объектов фигур
    rect, circle, square = create_shapes(n)

    # Вывод информации о фигурах
    print(rect)
    print(circle)
    print(square)

    # Пример работы с numpy
    print("Сумма элементов массива [1 2 3 4 5] равна {}".format(use_numpy_example()))


if __name__ == "__main__":
    main()
