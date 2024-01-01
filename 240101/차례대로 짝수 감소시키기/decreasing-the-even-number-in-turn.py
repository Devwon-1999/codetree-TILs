n = int(input())
num = 1000
even = 2
sum = 0
cnt = 0

while True:
    if num <= n:
        break
    else:
        num -= even
        sum += even
        even += 2
        cnt += 1

print(cnt, sum)