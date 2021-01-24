print('Введите список чисел через пробел: ')

list = sorted(list(map(float, input().split())))

print('Медиана списка: ', end='')
if len(list) % 2 == 0:
    print((list[len(list)//2 - 1] + list[len(list)//2]) / 2)
else:
    print(list[len(list)//2])
