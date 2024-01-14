def onjeon(num):
    if num % 2 == 0 or num % 10 == 5 or  (num % 3 == 0 and num % 9 != 0):
        return False
    else:
        return True


a, b = map(int, input().split())

cnt = 0

for i in range(a, b + 1):
    if onjeon(i):
        cnt += 1

print(cnt)