N, B = map(int, input().split())
result = []
while N > 0:
    digit = N % B
    N = N // B
    result.append(digit)

for i in range(len(result) - 1, -1, -1):
    print(result[i], end = "")