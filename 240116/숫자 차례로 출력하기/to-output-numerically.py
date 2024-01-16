def plus(N):
    if N == 0:
        return
    plus(N - 1)    
    print(N, end = " ")
    

def minus(N):
    if N == 0:
        return
    print(N, end = " ")
    minus(N - 1)


N = int(input())
plus(N)
print()
minus(N)