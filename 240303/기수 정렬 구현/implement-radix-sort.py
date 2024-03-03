n = int(input())
arr = list(map(int, input().split()))

max_val = max(arr)

exp = 1
while max_val // exp > 0:
    count = [0] * 10
    output = [0] * n

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]

    exp *= 10


print(*arr)