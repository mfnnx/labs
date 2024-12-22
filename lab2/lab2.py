import sys
import math

class SquareRoots:

    def __init__(self):
        '''
        Конструктор класса
        '''
        # Объявление коэффициентов
        self.coef_A = 0.0
        self.coef_B = 0.0
        self.coef_C = 0.0
        # Количество корней
        self.num_roots = 0
        # Список корней
        self.roots_list = set()

    def get_coef(self, index, prompt):
        try:
            coef_str = sys.argv[index]
        except:
            print(prompt)
            coef_str = input()
        coef = float(coef_str)
        return coef

    def get_coefs(self):
        '''
        Чтение трех коэффициентов
        '''
        self.coef_A = self.get_coef(1, 'Введите коэффициент А:')
        self.coef_B = self.get_coef(2, 'Введите коэффициент B:')
        self.coef_C = self.get_coef(3, 'Введите коэффициент C:')

    def calculate_roots(self):
        '''
        Вычисление корней квадратного уравнения
        '''
        a = self.coef_A
        b = self.coef_B
        c = self.coef_C
        # Вычисление дискриминанта и корней
        D = b ** 2 - 4 * a * c

        if D > 0.0:
            t1 = (-b + math.sqrt(D)) / (2 * a)
            t2 = (-b - math.sqrt(D)) / (2 * a)

            if t1 >= 0:
                self.roots_list.add(math.sqrt(t1))  # x1
                self.roots_list.add(-math.sqrt(t1))  # x2
            if t2 >= 0:
                self.roots_list.add(math.sqrt(t2))  # x3
                self.roots_list.add(-math.sqrt(t2))  # x4

        elif D == 0.0:
            t = -b / (2 * a)

            if t >= 0:
                self.roots_list.add(math.sqrt(t))  # x1
                self.roots_list.add(-math.sqrt(t))  # x2

        self.num_roots = len(self.roots_list)

    def print_roots(self):

        roots = sorted(self.roots_list)
        if len(roots) == 0:
            print('Нет действительных корней')
        elif len(roots) == 1:
            print('Один корень: {}'.format(roots[0]))
        elif len(roots) == 2:
            print('Два корня: {} и {}'.format(roots[0], roots[1]))
        elif len(roots) == 3:
            print('Три корня: {}, {}, и {}'.format(roots[0], roots[1], roots[2]))
        elif len(roots) == 4:
            print('Четыре корня: {}, {}, {}, и {}'.format(roots[0], roots[1], roots[2], roots[3]))

def main():
    # Создание объекта класса
    r = SquareRoots()
    # Последовательный вызов необходимых методов
    r.get_coefs()
    r.calculate_roots()
    r.print_roots()

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

