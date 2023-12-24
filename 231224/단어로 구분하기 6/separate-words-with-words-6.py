strList = list(input().split())
index = 0
for i in range(len(strList)):
    if (i + 1) % 3 == 0:
        print(strList[i])