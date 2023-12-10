inputStr = input()
result = []
for i in range(len(inputStr)):
    if i % 2 == 1:
        result.append(inputStr[i])

result.reverse()

for i in result:
    print(i, end="")