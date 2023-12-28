n = int(input())
numList = list(map(int, input().split()))
result = [0 for _ in range(8)]


for i in numList:
    if i == 1:
        result[0] += 1
    elif i == 2:
        result[1] += 1
    elif i == 3:
        result[2] += 1
    elif i == 4:
        result[3] += 1
    elif i == 5:
        result[4] += 1
    elif i == 6:
        result[5] += 1
    elif i == 7:
        result[6] += 1
    elif i == 8:
        result[7] += 1
    
for i, value in enumerate(result):
    print(i + 1, "-" ,value)