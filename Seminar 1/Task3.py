print('Введите список чисел через пробел: ')

raw_list = input().split()
list = []
for i in raw_list:
    list.append(float(i))

print('Список в обратном порядке: ', list[::-1])
