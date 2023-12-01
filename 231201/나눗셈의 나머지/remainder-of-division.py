a, b = map(int,input().split())
remainList = list()
cntList = [0 for i in range(10)]
add = 0
while a >= 1:
    remain = a % b
    remainList.append(remain)
    a //= b

for i in remainList:
    if i == 0:
        cntList[0] += 1
    elif i == 1:
        cntList[1] += 1
    elif i == 2:
        cntList[2] += 1
    elif i == 3:
        cntList[3] += 1
    elif i == 4:
        cntList[4] += 1
    elif i == 5:
        cntList[5] += 1
    elif i == 6:
        cntList[6] += 1
    elif i == 7:
        cntList[7] += 1
    elif i == 8:
        cntList[8] += 1
    elif i == 9:
        cntList[9] += 1

for i in cntList:
    if i == 0:
        continue
    add += i ** i
print(add)