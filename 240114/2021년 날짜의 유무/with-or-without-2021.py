def date_check(month, day):
    monthList31 = [1, 3, 5, 7, 8, 10, 12]
    monthList30 = [4, 6, 9, 11]
    monthList28 = [2]
    if 1 <= month <= 12 and 1 <= day <= 31:
        if month in monthList31 and 1 <= day <= 31:
            return True
        elif month in monthList30 and 1 <= day <= 30:
            return True
        elif month in monthList28 and 1 <= day <= 28:
            return True
        else:
            return False
    else:
        return False


M, D = map(int, input().split())

if date_check(M, D):
    print("Yes")
else:
    print("No")