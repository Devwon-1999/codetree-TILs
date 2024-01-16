def func(N):
    if N == 1:
        return 0

    if N % 2 == 0:
        return func(N // 2) + 1
    else:
        return func(N // 3) + 1


N = int(input())

print(func(N))