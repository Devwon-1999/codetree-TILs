n = input()
list_2 = []

for i in n:
    list_2.append(i)

num = 0
for i in list_2:
    i = int(i)
    num = num * 2 + i

print(num)