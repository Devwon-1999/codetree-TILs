n = int(input())

classroom = 0
bokdo = 0
tolet = 0

for i in range(1, n+1):
    if i % 12 == 0:
        tolet += 1
    elif i % 3 == 0:
        bokdo += 1
    elif i % 2 == 0:
        classroom += 1

print(classroom, bokdo, tolet)