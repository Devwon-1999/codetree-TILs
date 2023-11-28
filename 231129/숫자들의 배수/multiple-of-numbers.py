cnt = 0
index = 1
n = int(input())
arr = [0 for i in range(10)]
arr[0] = n

for i in range(2, 11):
    arr[index] = arr[0] * i
    index += 1

for i in arr:
    if i % 5 == 0:
        cnt += 1
    print(i,end = " ")
    if cnt == 2:
        break