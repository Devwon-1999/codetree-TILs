n, t = input().split()

n = int(n)

strList = []
result = []
cnt = 0
for i in range(n):
    temp = input()
    strList.append(temp)

for i in strList:
    if i[3] == t:
        cnt += 1
        result.append(i)

print(cnt)
for i in result:
    print(i)