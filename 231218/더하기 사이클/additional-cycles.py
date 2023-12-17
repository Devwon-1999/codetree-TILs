n = int(input())
cnt = 2
ten = n // 10
one = n % 10
temp = one + ten
com = (one*10) + (temp%10)
while True:
    ten = com // 10
    one = com % 10
    temp = one + ten

    com = (one*10) + (temp%10)

    if n == com:
        print(cnt)
        break
    else:
        cnt += 1