n = int(input())

base = [i for i in range(1, n + 1)]

move = []
for i in range(n):
    temp = int(input())
    move.append(temp)

cnt = 0
for index, value in enumerate(move):
    if value != 0:
        continue
    else:
        for i in move:
            if i == base[index]:
                cnt += 1
print(cnt + 1)