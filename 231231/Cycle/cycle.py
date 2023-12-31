N, P = map(int, input().split())

seen = []
current = N
cnt = 0

while current not in seen:
    seen.append(current)
    current = (current * N) % P
    cnt += 1

result = cnt - seen.index(current)
print(result)