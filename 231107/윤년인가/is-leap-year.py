year = int(input())

if (year % 400 == 0) or (year % 4 == 0):
    print("true")
elif year % 100 == 0:
    print("false")