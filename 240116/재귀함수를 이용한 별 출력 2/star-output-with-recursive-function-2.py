def func(N):
    if N == 0:
        return
    print("* " * N)
    func(N - 1)
    print("* " * N)



N = int(input())
func(N)