#a = list(map(float, input().strip().split()))
a = [1, 3, 2, 6, 4, 5, 35, 1, 1, 1, 12, 24, 45]
S = [0] * len(a)

S[0] = a[0]
S[1] = a[1]

for i in range(2, len(S)):
    S[i] = min(S[i-1], S[i-2]) + a[i]

route = [len(S)]
pos = len(S)-1

for i in range(len(S)-1, 1, -1):
    if S[i-1] > S[i-2] and i == pos:
        route.append(i-1)
        pos = i-2
    elif i == pos:
        route.append(i)
        pos = i-1

print('a =', a)
print('S = ', S, '\n\n', 'Путь:', sep='')

for i in route[::-1]:
    print(f' {i}-я ступенька')
