a, b = input().split()

lista = list(a)
listb = list(b)
resulta = []
resultb = []
tempa = ""
tempb = ""
for i in lista:
    if i.isdigit():
        i = int(i)    
        if 0 <= i <= 9:
            resulta.append(i)
    else:
        break

for i in listb:
    if i.isdigit():
        i = int(i)    
        if 0 <= i <= 9:
            resultb.append(i)
    else:
        break
        
for i in resulta:
    i = str(i)
    tempa += i
for i in resultb:
    i = str(i)
    tempb += i

tempa = int(tempa)
tempb = int(tempb)

print(tempa + tempb)