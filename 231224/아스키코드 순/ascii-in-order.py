n = int(input())
result = "z"
for i in range(n):
    temp = input()
    if ord(temp[0]) < ord(result[0]):
        result = temp

print(result)