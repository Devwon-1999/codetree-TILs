N = int(input())

base = []

for i in range(N):
    temp = list(map(int, input().split()))
    base.append(temp)

value = []
for i in range(N - 1):
    for j in range(N - 2):
        temp = 0
        for k in range(3):
            temp += base[i][j + k]
        value.append(temp)

max_value1 = max(value)
value.remove(max_value1)
max_value2 = max(value)
value.remove(max_value2)
print(max_value1 + max_value2)