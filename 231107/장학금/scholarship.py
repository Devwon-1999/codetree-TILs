mid, fin = map(int, input().split())

if mid >= 90 and fin >= 95:
    print(100000)
elif mid >= 90 and fin >= 90:
    print(50000)
else:
    print(0)