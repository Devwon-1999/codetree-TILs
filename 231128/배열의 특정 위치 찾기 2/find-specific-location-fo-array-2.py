arr = list(map(int, input().split()))
first = 0
second = 0
for i in range(0, 10, 2):
    first += arr[i]

for i in range(1, 10, 2):
    second += arr[i]

if first > second:
    print(first - second)
else:
    print(second - first)