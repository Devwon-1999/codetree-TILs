N = int(input())

passenger = []
for i in range(N):
    temp = list(map(int, input().split()))
    passenger.append(temp)

sorted_passenger = sorted(passenger, key = lambda x: x[0])

time = 0
for start, end in sorted_passenger:
    if time <= start:
        time = start
    time += end
print(time)