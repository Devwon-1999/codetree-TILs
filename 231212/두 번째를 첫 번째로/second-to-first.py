str = input()

a = str[0]
b = str[1]

strList = list(str)

for i in range(len(strList)):
    if strList[i] == b:
        strList[i] = a

s = "".join(strList)

print(s)