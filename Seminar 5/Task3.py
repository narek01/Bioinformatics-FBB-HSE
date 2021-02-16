string = input()
lines = ['$' + string]  # Затравочка для списка со сдвигами
result = list()

for i in range(len(string)):
    str = string[i:] + '$' + string[:i] # Генерируем список сдвигов
    lines.append(str)

lines.sort()

for line in lines:
    result.append(len(line) - line.find('$')) # Считаем положение "$" справа

print(result)
