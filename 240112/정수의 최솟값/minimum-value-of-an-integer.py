def min_value_print(a, b, c):
    numList = [a, b, c]

    print(min(numList))

a, b, c = map(int, input().split())
min_value_print(a, b, c)