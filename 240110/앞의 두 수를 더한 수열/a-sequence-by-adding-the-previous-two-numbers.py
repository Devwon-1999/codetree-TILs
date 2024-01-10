n = int(input())

numList = [0, 1]
start = 2
for i in range(n + 1):
    numList.append(numList[start - 1] + numList[start - 2])
    start += 1

print(numList[n])