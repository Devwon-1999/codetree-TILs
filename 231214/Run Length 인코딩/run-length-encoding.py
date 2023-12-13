inputString = input()
result = ""
count = 1

for i in range(1, len(inputString)):
    if inputString[i] == inputString[i-1]:
        count += 1
    else:
        result += inputString[i-1] + str(count)
        count = 1
    if i == len(inputString) - 1:
        result += inputString[i] + str(count)

if inputString:
    result += inputString[-1] + str(count)

print(len(result))
print(result)