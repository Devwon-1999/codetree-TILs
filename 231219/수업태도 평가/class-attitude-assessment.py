N = int(input())
dic = {"Bessie": 0, "Elsie": 0, "Daisy": 0, "Gertie": 0, "Annabelle": 0, "Maggie": 0, "Henrietta": 0}
for i in range(N):
    name, score = input().split()
    score = int(score)
    if name in dic:
        dic[name] += score

removeMinValue = min(dic.values())
dic = {key: value for key, value in dic.items() if value != removeMinValue}

resultValue = min(dic.values())
resultKey = [key for key, value in dic.items() if value == resultValue]
print(resultKey[0])