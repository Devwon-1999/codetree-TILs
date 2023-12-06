n = int(input())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

num = 1
jump = 1
for i in range(n):
    for j in range(n):
        arr[i][j] = num
        num += n
    num = jump + 1
    jump += 1
    
for i in range(n):
    for j in range(n):
        print(arr[i][j], end=" ")
    print()