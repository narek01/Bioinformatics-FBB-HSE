print('Введите список чисел через пробел: ')

raw_list = input().split()
list = []
for i in raw_list:
    list.append(float(i))
list = sorted(list)

print('Медиана списка: ', end='')
if len(list) % 2 == 0:
    print((list[int(len(list)/2) - 1] + list[int(len(list)/2)]) / 2)
else:
    print(list[int(len(list)/2)])
