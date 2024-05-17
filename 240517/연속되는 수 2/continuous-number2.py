n = int(input())
base = []
for i in range(n):
    temp = int(input())
    base.append(temp)
result = []
cnt = 0
if n == 1:
    print(1)
else:
    for i in range(len(base)):
        if i + 1 >= len(base):
            break

        if base[i] == base[i + 1]:
            cnt += 1

        else:
            result.append(cnt)
            cnt = 0
    result.append(cnt)
    print(max(result) + 1)