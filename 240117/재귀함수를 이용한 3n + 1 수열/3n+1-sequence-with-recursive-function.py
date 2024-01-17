def func(n):
    global cnt
    if n == 1:
        return cnt
    if n % 2 == 1:
        cnt += 1
        return func(n * 3 + 1)
    else:
        cnt += 1
        return func(n // 2)

n = int(input())
cnt = 0
print(func(n))