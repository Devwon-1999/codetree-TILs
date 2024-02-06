def print_odd_numbers(n):
    if n <= 369:
        
        if n % 2 != 0:
            print(n, end=" ")
        if n != 369:
            print_odd_numbers(n + 2)
    else:
        if n != 369:
            print_odd_numbers(n - 2)
        if n % 2 != 0:
            print(n, end=" ")


n = int(input())
print_odd_numbers(n)