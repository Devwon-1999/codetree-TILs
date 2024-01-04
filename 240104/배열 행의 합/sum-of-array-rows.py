baseList = []
for i in range(5):
    temp = list(map(int, input().split()))
    baseList.append(temp)

for i in baseList:
    print(sum(i))