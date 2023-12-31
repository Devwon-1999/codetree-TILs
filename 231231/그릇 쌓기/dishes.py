s = input()
result = 10
for i in range(len(s)-1):
    if s[i] + s[i - 1] == "))" or s[i] + s[i - 1] == "((":
        result += 5
    elif s[i] + s[i - 1] == "()" or s[i] + s[i - 1] == ")(":
        result += 10

print(result)