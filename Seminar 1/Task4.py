n = int(input('Введите число N: '))
print('Введите сравниваемые числа: ')
t = float(input())
for i in range(1, n):
    inp = float(input())
    t = inp if (inp > t) else t
print('Наибольшее число: ', t)
