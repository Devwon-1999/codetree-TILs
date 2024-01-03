n = int(input())
abcList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
strList = list(input().split())
resultList = []
tempList = []

for i in strList:
    if i in abcList:
        resultList.append(i)
    else:
        break

resultList.sort()

for i in resultList:
    if i not in tempList:
        tempList.append(i)

for i in tempList:
    print(f"{i} : {resultList.count(i)}")