def day_of_week(month, day):
    days_of_week = ["Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri"]

    elapsed_days = 0
    for m in range(1, month):
        elapsed_days += num_of_days[m]

    elapsed_days += day - 1

    return days_of_week[(elapsed_days + 5) % 7]


m1, d1, m2, d2 = map(int, input().split())

num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if m1 == m2 and d1 == d2:
    result = day_of_week(m2, d2)
else:
    if (m1 == m2 and d1 <= d2) or (m1 < m2):
        result = day_of_week(m2, d2)
    else:
        result = day_of_week(m2, d2)
print(result)