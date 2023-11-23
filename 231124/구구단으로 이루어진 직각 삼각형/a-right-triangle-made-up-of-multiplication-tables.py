n = int(input())
m = n
for i in range(1, n+1):
    for j in range(1, m+1):
        if j == m:
            print(f"{i} * {j} = {i * j}")
        else:
            print(f"{i} * {j} = {i * j}", end=" / ")
    m -= 1