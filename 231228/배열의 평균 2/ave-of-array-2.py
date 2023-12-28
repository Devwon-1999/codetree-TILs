numList = []

for i in range(3):
    temp1 = list(map(int, input().split()))
    numList.append(temp1)

for i in numList:
    print("%.1f" % (sum(i)/3), end = " ")
print()

temp2 = 0
for i in range(3):
    temp2 = 0
    for j in range(3):
        temp2 = temp2 + numList[j][i]
    print("%.1f" % (temp2/3), end = " ")
print()

temp3 = 0
for i in numList:
    for j in i:
        temp3 += j

print("%.1f" % (temp3 / 9))