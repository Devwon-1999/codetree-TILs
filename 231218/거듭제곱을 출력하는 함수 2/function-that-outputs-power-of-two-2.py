a, b = map(int, input().split())

first = a ** b
second = b ** a

if first > second:
    print(first - second)
else:
    print(second - first)