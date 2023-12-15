n = int(input())
tempList = []
result = 0
for i in range(n):
    temp = int(input())
    tempList.append(temp)

for i in tempList:
    result += i

result = str(result)

result = result[1:]+result[0]

print(result)