def sumArr(arr, n):

    for i in arr:
        i.append(sum(i))

    tempList = []
    index = 0
    for i in range(n + 1):
        total = 0
        for j in range(n):
            total += arr[j][index]
        index += 1
        tempList.append(total)
    arr.append(tempList)

    for i in arr:
        for j in i:
            print(j, end = " ")
        print()


n = int(input())

inputList = []

for i in range(n):
    temp = list(map(int, input().split()))
    inputList.append(temp)

sumArr(inputList, n)