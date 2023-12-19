n = int(input())
cnt = 65 + (n * n) - 1
# if cnt > 90:
#     temp = cnt - 90
#     cnt = temp + 65 - 1
first = cnt
for i in range(n):
    for j in range(n):
        if cnt > 90:
            cnt = 65
        elif cnt < 65:
            temp = 65 - cnt
            cnt = 90 - temp + 1
        print(chr(cnt), end=" ")
        
        cnt = cnt - n
    print()
    cnt = first - (i + 1)