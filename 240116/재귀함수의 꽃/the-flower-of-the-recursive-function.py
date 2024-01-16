def func(N):
    if N == 0:
        return 0

    print(N, end = " ")
    func(N - 1)
    print(N, end = " ")


N = int(input())

func(N)