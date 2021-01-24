n = int(input('Введите число N: '))
print('Введите сравниваемые числа: ')
max = float(input())
t = max

for i in range(1, n):
    inp = float(input())
    if inp > max:
        t = max
        max = inp
    if ((inp > t or t == max) and inp < max):
        t = inp
print('Второе по величине число: ', t)
