s = input()
result = ""
for i in s:
    if i.isalpha():
        result += i
result = result.lower()
print(result)