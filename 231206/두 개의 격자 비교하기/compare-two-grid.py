n, m = map(int, input().split())

arr1 = [
    [0 for _ in range(m)]
    for _ in range(n)
]

arr2 = [
    [0 for _ in range(m)]
    for _ in range(n)
]

temparr = [
    [0 for _ in range(m)]
    for _ in range(n)
]


for i in range(n):
    tempList = list(map(int, input().split()))
    for j in range(m):
        arr1[i][j] = tempList[j]

for i in range(n):
    tempList = list(map(int, input().split()))
    for j in range(m):
        arr2[i][j] = tempList[j]

for i in range(n):
    for j in range(m):
        if arr1[i][j] == arr2[i][j]:
            print(0,end=" ")
        else:
            print(1,end=" ")
    print()