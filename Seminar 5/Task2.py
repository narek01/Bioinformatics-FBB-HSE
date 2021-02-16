string = input()
lines = list()
out = str()

for i in range(len(string)):
    shift = string[i:] + string[:i]  # Список всех сдвигов
    lines.append(shift)
lines.sort()

print(lines)

for line in lines:
    out += line[-1] # Берём по последнему символу из каждой строки
print(out)
