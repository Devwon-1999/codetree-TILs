def printHolJjack(n):
    if n % 2 == 0:
        for i in range(2, n + 1, 2):
            print(i, end = " ")
    else:
        for i in range(1, n + 1, 2):
            print(i, end = " ")
            
n = int(input())

printHolJjack(n)