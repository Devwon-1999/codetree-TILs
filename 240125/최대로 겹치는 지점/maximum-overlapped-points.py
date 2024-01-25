n = int(input())
temp = []
maxValue = 0
minValue = 0

for i in range(n):
    a, b = map(int, input().split())
    temp.append([a,b])

maxValue = max(max(temp))
minValue = min(min(temp))

result = [0 for i in range(minValue, maxValue + 1)]
    
for i in temp:
    for j in range(i[0], i[1] + 1):
        result[j - 1] += 1

print(max(result))