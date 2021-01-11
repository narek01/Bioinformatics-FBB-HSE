n = int(input('Введите число N: '))
print('Введите сравниваемые числа: ')
t = int(input())
for i in range(1, n):
    inp = int(input())
    t = inp if (inp > t) else t
print('Наибольшее число: ', t)
