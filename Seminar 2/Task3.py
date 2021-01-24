list = list(map(float, input().split()))
#list = [1,2,2,2,3,4,5,5,5,5,5,6,6,6,6,6,6,6,6,6,7,8,8,8,8,8,8,9,10,1000]
n = float(input())

def func(list):
    if n == list[len(list)//2-1]:
        return print('Yes')
    elif n > list[len(list)//2-1] and len(list) != 1:
        list = list[len(list)//2:]
        print(list)
        func(list)
    elif n < list[len(list)//2-1] and len(list) != 1:
        list = list[:len(list)//2]
        print(list)
        func(list)
    else:
        print('No')

if n < list[0] or n > list[len(list)-1]:
    print('No')
else:
    func(list)
