alpha = input()
alphaList = []

findword = input()
findList = []
for i in range(len(alpha)):
    alphaList.append(alpha[i])

for i in range(len(findword)):
    findList.append(findword[i])
cnt = 0
while True:
    for i in alphaList:
        for j in findList:
            if i == j:
                findList.remove(j)
                cnt += 1


    if findList:
        continue
    else:
        break

print(cnt)