n = int(input())

numList = list(map(int, input().split()))

numList.sort()
for i in numList:
    print(i, end = " ")

print()

numList.sort(reverse=True)
for i in numList:
    print(i, end = " ")