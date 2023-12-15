a = input()
lista = list(a)
addNum = 0
for i in lista:
    if i.isdigit():
        i = int(i)
        addNum += i
print(addNum)