day, hour, mins = 11, 11, 11
a, b, c = map(int, input().split())
elapsed_time = 0
if day <= a and hour <= b and mins <= c:
    while True:
        if day == a and hour == b and mins == c:
            break

        elapsed_time += 1
        mins += 1

        if mins == 60:
            hour += 1
            mins = 0
        if hour == 24:
            day += 1
            hour = 0

    print(elapsed_time)
else:
    print(-1)