cnt_0 = 0
cnt_1 = 0
def codetree(n):
    global cnt_0
    global cnt_1
    if n == 0:
        cnt_0 += 1
        return 0
    elif n == 1:
        cnt_1 += 1
        return 1
    else:
        return codetree(n - 1) + codetree(n - 2)

n = int(input())

codetree(n)

print(cnt_0,cnt_1)