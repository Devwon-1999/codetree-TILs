a = input()
b = input()
resulta = ""
resultb = ""
for i in a:
    if i.isalpha():
        continue
    if i.isdigit():
        resulta += i

for i in b:
    if i.isalpha():
        continue
    if i.isdigit():
        resultb += i

resulta = int(resulta)
resultb = int(resultb)
print(resulta + resultb)