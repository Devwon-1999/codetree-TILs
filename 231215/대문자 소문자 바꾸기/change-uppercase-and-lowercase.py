a = input()
resultList = []
for i in a:
    if ord(i) >= 65 and ord(i) <= 90:
        resultList.append(ord(i) + 32)
    elif ord(i) >= 97 and ord(i) <= 122:
        resultList.append(ord(i) - 32)


for i in resultList:
    print(chr(i),end="")