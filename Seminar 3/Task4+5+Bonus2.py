# Ввод сиквенсов
seq1 = input('Введите последовательность 1: ').replace(' ', '').replace('\n', '')
seq2 = input('Введите последовательность 2: ').replace(' ', '').replace('\n', '')

# Настроечка алгоритма
d = 10
e = 0.5
match = 5
mismatch = -4


def zero_matrix(matrix, i, j):
    for k in range(i):
        zero_row = [0] * j
        matrix.append(zero_row)

def match_check(seq1, seq2):
    if seq1 == seq2:
        return match
    else:
        return mismatch

# Создаём нулевые матрицы
A, B, S, D = [], [], [], []
zero_matrix(A, len(seq1), len(seq2))
zero_matrix(B, len(seq1), len(seq2))
zero_matrix(S, len(seq1)+1, len(seq2)+1)
zero_matrix(D, len(seq1)+1, len(seq2)+1) # Матрица со стрелками

# Инициализируем матрицы
for i in range(len(seq1)):
    S[i+1][0] = -d - e*i
    B[i][0] = S[i+1][0]-d
for j in range(len(seq2)):
    S[0][j+1] = -d - e*j
    A[0][j] = S[0][j+1]-d

for i in range(len(seq1)):
    for j in range(len(seq2)):
        S[i+1][j+1] = max(A[i][j], B[i][j], S[i][j] + match_check(seq1[i], seq2[j]))

        if A[i][j] > B[i][j] and A[i][j] > match_check(seq1[i], seq2[j]):
            D[i+1][j+1] = '↓'
        elif B[i][j] > A[i][j] and B[i][j] > match_check(seq1[i], seq2[j]):
            D[i+1][j+1] = '→'
        else:
            D[i+1][j+1] = '↘'

        if i != len(seq1)-1:
            A[i+1][j] = max(A[i][j]-e, S[i+1][j+1]-d)
        if j != len(seq2)-1:
            B[i][j+1] = max(B[i][j]-e, S[i+1][j+1]-d)


check = [len(seq1), len(seq2)]
al_u, al_d = '', ''

for i in range(len(seq1), 0, -1):
    for j in range(len(seq2), 0, -1):
        if i == check[0] and j == check[1]:
            if D[i][j] == '↘':
                if i == 1 and j != 1:
                    al_d += seq2[j-1]
                    al_u += '-'
                    check = [i, j-1]
                elif i != 1 and j == 1:
                    al_d += '-'
                    al_u += seq1[i-1]
                    check = [i-1, j]
                else:
                    al_d += seq2[j-1]
                    al_u += seq1[i-1]
                    check = [i-1, j-1]
            elif D[i][j] == '↓':
                al_d += '-'
                al_u += seq1[i-1]
                check = [i-1, j]
            elif D[i][j] == '→':
                al_d += seq2[j-1]
                al_u += '-'
                check = [i, j-1]
        if i == 1 and j == 1:
            break
for i in S:
    print(i)
print('\n', al_u[::-1], sep='')
print(al_d[::-1], '\n')
print('Score: ', S[len(seq1)][len(seq2)], '\n')
