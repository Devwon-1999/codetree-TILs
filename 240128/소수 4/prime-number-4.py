n, k = map(int, input().split())

base = [i for i in range(2, n + 1)]
index = 0
result = []
while True:
    if base:
        del_num = base[0]
        for i in base:
            if i % del_num == 0:
                base.remove(i)
                result.append(i)
    else:
        break
print(result[k - 1])