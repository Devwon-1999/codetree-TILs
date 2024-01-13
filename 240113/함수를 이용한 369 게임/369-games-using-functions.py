def three_six_nine(n):
    if n % 10 == 3 or n % 10 == 6 or n % 10 == 9 or n // 10 == 3 or n // 10 == 6 or n // 10 == 9:
        return 1
    else:
        return 0


def three_mul(n):
    if n % 3 == 0:
        return 1
    else:
        return 0


a, b = map(int, input().split())
cnt = 0

for i in range(a, b + 1):
    if three_six_nine(i) == 1 or three_mul(i) == 1:
        cnt += 1
print(cnt)