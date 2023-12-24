a = input()

eeTrue = "NO"
eaTrue = "NO"
for i in range(len(a)):
    if i + 1 > len(a):
        break
    if a[i] == "e" and a[i+1] == "e":
        eeTrue = "YES"
    if a[i] == "e" and a[i+1] == "a":
        eaTrue = "YES"
    

print(eeTrue, eaTrue)