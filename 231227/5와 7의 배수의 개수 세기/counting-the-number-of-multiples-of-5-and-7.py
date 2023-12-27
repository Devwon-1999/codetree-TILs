n = int(input())

numList = list(map(int, input().split()))
cnt5 = 0
cnt7 = 0
for i in numList:
    if i % 5 == 0:
        cnt5 += 1
    if i % 7 == 0:
        cnt7 += 1

print(cnt5)
print(cnt7)