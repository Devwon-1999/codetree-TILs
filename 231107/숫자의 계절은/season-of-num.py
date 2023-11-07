month = int(input())

if 3 <= month <= 5:
    print("Spring")

elif 6 <= month <= 8:
    print("Summer")

elif 9 <= month <= 11:
    print("Fall")

elif month == 1 or month == 2 or month == 12:
    print("Winter")