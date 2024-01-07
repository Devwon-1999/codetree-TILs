arr1 = []
arr2 = []

for i in range(4):
    temp = list(map(int, input().split()))
    arr1.append(temp)

trash = input()

for i in range(4):
    temp = list(map(int, input().split()))
    arr2.append(temp)

for i in range(4):
    for j in range(2):
        print(arr1[i][j] * arr2[i][j], end = " ")
    print()