N = int(input())

base = [0 for i in range(101)]
value = []
for i in range(N):
    x1, x2 = map(int, input().split())
    value.append([x1, x2])
    for j in range(x1, x2 + 1):
        base[j] += 1

result = []
for i in range(N):
    for x1, x2 in value:
        temp = base[:]
        for j in range(x1, x2 + 1):
            temp[j] -= 1
            
        for h in temp:
            if h == N - 1:
                result.append(1)
                break
            else:
                continue
        if result:
            break
    if result:
        break

if result:
    print("Yes")
else:
    print("No")