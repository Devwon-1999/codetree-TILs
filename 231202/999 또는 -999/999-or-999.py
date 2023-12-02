arr=list(map(int,input().split()))
resultArr= list()

for i in arr:
    if i==999 or i == -999:
        break
    resultArr.append(i)

print(max(resultArr), min(resultArr))