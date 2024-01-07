def sumFromTen(n):
    result = 0
    for i in range(10, n + 1):
        result += i

    print(result)


n = int(input())

sumFromTen(n)