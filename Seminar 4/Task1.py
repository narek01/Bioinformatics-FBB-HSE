x = [-1, -1, 0, 1, 2, -10, -4, 9, 1, 0, -1, 3, -10]
x = [2, -1, 3, 4, -100]

S = [0] * len(x)
S[0] = x[0]
for i in range(1, len(S)):
    S[i] = max(S[i - 1] + x[i], x[i])

left = 0
for i in range(S.index(max(S)), 0, -1):
    if S[i-1] < 0:
        left = i
        break

print('Границы подмассива: от', left, 'до', S.index(max(S)), '(отсчёт с нуля)')
print(S)
