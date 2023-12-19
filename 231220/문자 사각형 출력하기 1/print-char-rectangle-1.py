n = int(input())
cnt = 64
for i in range(n * n):
    cnt += 1
    if cnt > 90:
        cnt = 65

first = cnt
for i in range(n):
    for j in range(n):
        if cnt > 90:
            cnt = 65
        elif cnt < 65:
            temp = 65 - cnt
            cnt = 90 - temp
        print(chr(cnt), end=" ")
        cnt = cnt - n
    print()
    cnt = first - (i + 1)