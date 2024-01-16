def func(N):
    if N == 1:
        return 1
    if N == 2:
        return 1
    
    return func(N - 1) + func(N - 2)


N = int(input())

print(func(N))