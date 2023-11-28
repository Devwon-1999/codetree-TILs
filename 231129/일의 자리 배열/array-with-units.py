a, b = map(int, input().split())

list = [0 for i in range(10)]
list[0] = a
list[1] = b

for i in range(2, 10):
    list[i] = list[i-1] + list[i-2]
    if list[i] >= 10:
        list[i] = list[i] % 10

for i in list:
    print(i,end=" ")