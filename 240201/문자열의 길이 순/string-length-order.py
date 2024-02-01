n = int(input())
strList = []

for i in range(n):
    temp = input()
    strList.append(temp)

strList.sort(key=lambda x: (len(x), x))

for string in strList:
    print(string)