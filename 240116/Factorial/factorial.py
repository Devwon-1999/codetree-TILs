def factorial(N):
    if N == 1:
        return 1

    return factorial(N-1) * N


N = int(input())

print(factorial(N))