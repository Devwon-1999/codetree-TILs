strList = []

for i in range(5):
    temp = input()
    temp += "                             "
    strList.append(temp)

for i in range(15):
    for j in range(5):
        if strList[j][i] == " ":
            pass
        else:
            print(strList[j][i], end="")