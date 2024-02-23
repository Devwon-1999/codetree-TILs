N = int(input())

base = [0 for i in range(101)]
for i in range(N):
    x1, x2 = map(int, input().split())
    for j in range(x1, x2 + 1):
        base[j] += 1
check = False
for i in base:
    if i == 0 or i == 1:
        continue
    else:
        check = True
        break
if check:
    print("Yes")
else:
    print("No")