def even_and_5mul(n):
    if n % 2 == 0 and ((n // 10) + (n % 10)) % 5 == 0:
        print("Yes")
    else:
        print("No")


n = int(input())

even_and_5mul(n)