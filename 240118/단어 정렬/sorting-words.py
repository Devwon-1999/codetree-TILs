n = int(input())
strList = []
for i in range(n):
    string = input()
    strList.append(string)

strList.sort()

for i in strList:
    print(i)