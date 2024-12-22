from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square
import numpy as np

def main():
    n = 22  

    # Создание объектов
    rect = Rectangle(n, n, "синий")
    circle = Circle(n, "зеленый")
    square = Square(n, "красный")

    # Вывод информации о фигурах
    print(rect)
    print(circle)
    print(square)

    # Использование внешнего пакета numpy
    arr = np.array([1, 2, 3, 4, 5])
    print("Использование numpy: сумма элементов массива {} равна {}".format(arr, np.sum(arr)))

if __name__ == "__main__":
    main()
