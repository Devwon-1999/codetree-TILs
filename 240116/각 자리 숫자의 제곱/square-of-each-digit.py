def func(N):
    if N < 10:
        return N ** 2

    return func(N // 10) + ((N % 10) ** 2 )


N = int(input())

print(func(N))