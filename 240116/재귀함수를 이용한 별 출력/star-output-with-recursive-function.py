def func(N):
    if N == 0:
        return

    func(N - 1)
    print("*" * N)


N = int(input())
func(N)