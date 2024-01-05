n = int(input())
result = [1, n]
x, y = 0, 1

while True:
    newValue = result[x] + result[y]
    result.append(newValue)
    if newValue >= 1000:
        break
    x += 1
    y += 1

for i in result:
    print(i, end = " ")