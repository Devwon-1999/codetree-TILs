n = int(input())

scoreList = list(map(int, input().split()))

result = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in scoreList:
    if i < 10:
        continue
    elif 10 <= i < 20:
        result[0] += 1
    elif 20 <= i < 30:
        result[1] += 1
    elif 30 <= i < 40:
        result[2] += 1
    elif 40 <= i < 50:
        result[3] += 1
    elif 50 <= i < 60:
        result[4] += 1
    elif 60 <= i < 70:
        result[5] += 1
    elif 70 <= i < 80:
        result[6] += 1
    elif 80 <= i < 90:
        result[7] += 1
    elif 90 <= i < 100:
        result[8] += 1  
    elif i == 100:
        result[9] += 1
result.reverse()

for i, value in enumerate(result):
    if value == 0:
        continue
    else:
        print(100 - (i * 10),"-",value)