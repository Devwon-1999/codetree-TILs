N = int(input())

strList = []

for i in range(N):
    temp = input()
    strList.append(temp)

for i in range(N - 1):
    temp = input()
    if temp in strList:
        strList.remove(temp)

print(strList[0])