a, b, c = float(input()), float(input()), float(input())

D = b**2 - 4*a*c

if a != 0:
    x1 = (-b + pow(D, 0.5)) / 2*a
    x2 = (-b - pow(D, 0.5)) / 2*a
    if x1 != x2:
        print('Уравнение имеет два корня: ', x1,' и ', x2, '.')
    else:
        print('Уравнение имеет один корень: ', x1, '.')
elif b == 0 and c == 0:
    print('x Є C - любое число')
elif b == 0:
    print('Решений нет')
else:
    print('Уравнение имеет один корень: ', -c/b, '.')
