X, Y = map(int, input().split())
cnt = 0
for i in range(X, Y + 1):
    a = i
    reverse_i = str(a)
    reverse_i = list(reverse_i)
    reverse_i.reverse()
    num = 0
    for j in reverse_i:
        num += int(j)
        num *= 10
    if i == num// 10:
        cnt += 1
print(cnt)