n = int(input())
numList = list(map(int, input().split()))

indexZero = numList.index(0)
result = 0

for i in numList[indexZero - 5:indexZero]:
    result += i

print(result)