import sys
import math

def get_coef(index, promt):
    try:
        coef_str = sys.argv[index]
    except:
        print(promt)
        coef_str = input()
    coef = float(coef_str)
    return coef


def get_roots(a, b, c):
    result = set()
    D = b ** 2 - 4 * a * c

    if D > 0.0:
        t1 = (-b + math.sqrt(D)) / (2 * a)
        t2 = (-b - math.sqrt(D)) / (2 * a)

        if t1 >= 0:
            result.add(math.sqrt(t1))  # x1
            result.add(-math.sqrt(t1))  # x2
        if t2 >= 0:
            result.add(math.sqrt(t2))  # x3
            result.add(-math.sqrt(t2))  # x4

    elif D == 0.0:
        t = -b / (2 * a)

        if t >= 0:
            result.add(math.sqrt(t))  # x1
            result.add(-math.sqrt(t))  # x2

    return sorted(result)


def main():
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')

    roots = get_roots(a, b, c)
    len_roots = len(roots)

    if len_roots == 0:
        print('Нет действительных корней')
    elif len_roots == 1:
        print('Один корень: {}'.format(roots[0]))
    elif len_roots == 2:
        print('Два корня: {} и {}'.format(roots[0], roots[1]))
    elif len_roots == 3:
        print('Три корня: {}, {}, и {}'.format(roots[0], roots[1], roots[2]))
    elif len_roots == 4:
        print('Четыре корня: {}, {}, {}, и {}'.format(roots[0], roots[1], roots[2], roots[3]))

# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

