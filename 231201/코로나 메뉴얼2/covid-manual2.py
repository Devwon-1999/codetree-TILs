coldList = list()
resultList = list()
acnt = 0
bcnt = 0
ccnt = 0
dcnt = 0
for i in range(3):
    a, b = input().split()
    b = int(b)
    coldList.append(a)
    coldList.append(b)

for i in range(6):
    if coldList[i] == "Y" and coldList[i+1] >= 37:
        resultList.append("A")
    elif coldList[i] == "N" and coldList[i+1] >= 37:
        resultList.append("B")
    elif coldList[i] == "Y" and coldList[i+1] < 37:
        resultList.append("C")
    elif coldList[i] == "N" and coldList[i+1] < 37:
        resultList.append("D")
    else:
        continue

for i in resultList:
    if i == "A":
        acnt += 1
    elif i == "B":
        bcnt += 1
    elif i == "C":
        ccnt += 1
    elif i == "D":
        dcnt += 1

print(acnt, bcnt, ccnt, dcnt, end=" ")
if acnt >= 2:
    print("E")