a = input()
index = 1
eeTrue = "NO"
eaTrue = "NO"
for i in a:
    if i == "e" and a[index] == "e":
        eeTrue = "YES"
    if i == "e" and a[index] == "a":
        eaTrue = "YES"
    index += 1
    if index > len(a):
        index -= 1

print(eeTrue, eaTrue)