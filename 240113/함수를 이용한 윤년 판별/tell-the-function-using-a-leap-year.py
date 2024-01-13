def year_check(y):
    if y % 400 == 0:
        return True
    elif y % 100 == 0:
        return False
    elif y % 4 == 0:
        return True

y = int(input())

result = year_check(y)

if result:
    print("true")
else:
    print("false")