s = input()
order = list(input())

for i in order:
    if i == "L":
        s = s[1:] + s[0]

    elif i == "R":
        s = s[-1] + s[0:len(s)-1]

print(s)