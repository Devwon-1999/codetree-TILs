N, K = map(int, input().split())


not_friendly = []

for i in range(K):
    temp = list(map(int, input().split()))
    not_friendly.append(temp)

print(not_friendly)