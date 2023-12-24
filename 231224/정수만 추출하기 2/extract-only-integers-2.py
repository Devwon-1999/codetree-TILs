a, b = input().split()
newA = ""
newB = ""
strainer = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
for i in a:
    if i in strainer:
        continue
    else:
        newA = newA + i

for i in b:
    if i in strainer:
        continue
    else:
        newB = newB + i

newA, newB = int(newA), int(newB)

print(newA + newB)