a = input()
index = 1
eeTrue = "NO"
eaTrue = "NO"
for i in a:
    if i == "e" and a[index] == "e":
        eeTrue = "YES"
    if i == "a" and a[index] == "e":
        eaTrue = "YES"
    if index == len(a):
        index -= 1
    else:
        index += 1

print(eeTrue, eaTrue)