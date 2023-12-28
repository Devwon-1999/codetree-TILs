n = int(input())
strList = []
for i in range(n):
    temp = input()
    strList.append(temp)

order = input()
resultList = []

cnt = 0
for i in strList:
    if i[-1] == order:
        cnt += 1
        resultList.append(i)
print(cnt)        
for i in resultList:
    print(i)