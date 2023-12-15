n, A = input().split()

n = int(n)
cnt = 0
for i in range(n):
    temp = input()
    if temp == A:
        cnt += 1

print(cnt)