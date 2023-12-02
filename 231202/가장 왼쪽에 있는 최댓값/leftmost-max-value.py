n = int(input())

arr = list(map(int,input().split()))

maxValue = n

while True:
    tempMax = 0
    for j in range(1, maxValue):
        if  arr[tempMax] < arr[j]:
            tempMax = j
    print(tempMax + 1,end=' ')

    if  tempMax == 0 :
        break
    
    maxValue = tempMax