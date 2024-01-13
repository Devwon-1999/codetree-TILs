def three_six_nine(n):
    numList = []
    for i in str(n):
        numList.append(i)

    if "3" in numList or "6" in numList or "9" in numList:
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