n = int(input())

arr = [0 for i in range(20)]

arr[0] = 1
arr[1] = n

for i in range(2, 20):
    arr[i] = arr[i-2] + arr[i-1]

for i in arr:
    print(i, end = ' ')
    if i >= 100:
        break