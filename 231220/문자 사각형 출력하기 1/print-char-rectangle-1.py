n = int(input())
cnt = 65 + (n * n) - 1
first = cnt
for i in range(n):
    for j in range(n):
        if cnt > 90:
            cnt = 65
        print(chr(cnt), end=" ")
        cnt = cnt - n
    print()
    cnt = first - (i + 1)