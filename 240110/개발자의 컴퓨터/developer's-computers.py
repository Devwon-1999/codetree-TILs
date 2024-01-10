N = int(input())
times = []

for _ in range(N):
    s, t, b = map(int, input().split())
    times.append((s, t, b))

computer_usage = [0] * 1001

for time in times:
    for i in range(time[0], time[1]):
        computer_usage[i] += time[2]

min_computers = max(computer_usage)

print(min_computers)