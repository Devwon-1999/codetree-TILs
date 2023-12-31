strList = []

for i in range(5):
    temp = input()
    strList.append(temp)

for i in range(3):
    for j in range(5):
        if strList[j][i] != "":
            print(strList[j][i],end="")
        else:
            continue