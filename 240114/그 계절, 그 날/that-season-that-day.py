def date_check(month, day, yc):
    if yc: # 윤년일때
        monthList31 = [1, 3, 5, 7, 8, 10, 12]
        monthList30 = [4, 6, 9, 11]
        monthList29 = [2]
        if 1 <= month <= 12 and 1 <= day <= 31:
            if month in monthList31 and 1 <= day <= 31:
                return True
            elif month in monthList30 and 1 <= day <= 30:
                return True
            elif month in monthList29 and 1 <= day <= 29:
                return True
            else:
                return False
        else:
            return False
    else: # 평년일때
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


def year_check(year):
    if year % 400 == 0:     #윤년
        return True 
    elif year % 100 == 0:   #평년
        return False
    elif year % 4 == 0:     #윤년
        return True
    else:                   #평년
        return False


def season_check(month):
    if 3 <= month <= 5:
        print("Spring")
    elif 6 <= month <= 8:
        print("Summer")
    elif 9 <= month <= 11:
        print("Fall")
    elif 1 <= month <= 2 or month == 12:
        print("Winter")


Y, M, D = map(int, input().split())

yc = year_check(Y)

if date_check(M, D, yc):
    season_check(M)
else:
    print(-1)