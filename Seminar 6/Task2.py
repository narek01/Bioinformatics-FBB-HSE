X = 'ATATATTAG'
S = [10, 8, 1, 3, 5, 9, 7, 2, 4, 6]
alphabet = '$ A T G C'.split()

X += '$'

def BWT(X, S):
    BWT_result = ''
    for i in range(len(S)):
        if S[i] == 1:
            BWT_result += "$"
        else:
            BWT_result += X[S[i] - 2]
    return BWT_result

def C(X, alphabet):
    for char in alphabet:
        count = 0
        for symbol in X:
            if symbol < char:
                count += 1
        print(f'C({char}) = {count}')

print(BWT(X, S))
C(X, alphabet)
