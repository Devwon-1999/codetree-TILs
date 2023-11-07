year = int(input())

if (year % 4 == 0) and (year % 100 != 0):
    print("true")
else:
    print("false")