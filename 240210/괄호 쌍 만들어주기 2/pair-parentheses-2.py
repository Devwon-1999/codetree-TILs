string = input()
strList = []

for i in string:
    strList.append(i)

cnt = 0

for i in range(len(strList) - 1):
    if strList[i] == "(" and strList[i + 1] == "(":
        for j in range(i + 2, len(strList) - 1):
            if strList[j] == ")" and strList[j + 1] == ")": 
                cnt += 1

print(cnt)