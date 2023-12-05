abcList = list()
for i in range(5):
    tempList =  list(map(lambda char: ord(char), ''.join(input().split())))
    abcList.append(tempList)

for i in range(5):
    for j in range(3):
        print(chr(abcList[i][j] - 32),end=" ")
    print()