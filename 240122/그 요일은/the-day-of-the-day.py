def day_of_week(year, month, day):
    days_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    elapsed_days = 0
    for y in range(2024, year):
        if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
            elapsed_days += 366
        else:
            elapsed_days += 365

    for m in range(1, month):
        elapsed_days += num_of_days[m]

    elapsed_days += day - 1

    return days_of_week[(elapsed_days + 1) % 7]


m1, d1, m2, d2 = map(int, input().split())
target_day = input().strip()

num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
count = 0
current_day = day_of_week(2024, m1, d1)

while not (m1 == m2 and d1 == d2):
    if current_day == target_day:
        count += 1

    d1 += 1
    if d1 > num_of_days[m1]:
        m1 += 1
        d1 = 1

    current_day = day_of_week(2024, m1, d1)

if current_day == target_day:
    count += 1

print(count)