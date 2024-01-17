def func(N):
    if N == 1:
        return 1
    if N == 2:
        return 2
    if N % 2 == 1:   #홀수
        return func(N - 2) + N


    else:            #짝수
        return func(N - 2) + N




N = int(input())

print(func(N))