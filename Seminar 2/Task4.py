list = list(map(float, input().split()))
#list = [1,3,7,-3,-10,0,0,1,1,578,13456,-1]

for i in range(len(list)):
    for j in range(1, len(list)-i):
        if list[j] < list[j-1]:
            list[j], list[j-1] = list[j-1], list[j]
print(list)
