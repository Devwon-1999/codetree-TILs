n = int(input())

for i in range(1, 11):
    if i * n > 200:
        break
    print(i * n, end = " ")
    if i * n % 10 == 0:
        break