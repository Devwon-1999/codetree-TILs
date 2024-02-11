def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    x_root = find(parent, x)
    y_root = find(parent, y)

    if rank[x_root] < rank[y_root]:
        parent[x_root] = y_root
    elif rank[x_root] > rank[y_root]:
        parent[y_root] = x_root
    else:
        parent[y_root] = x_root
        rank[x_root] += 1

def min_photos(N, dislikes):
    parent = [i for i in range(N + 1)]
    rank = [0] * (N + 1)

    for dislike in dislikes:
        a, b = dislike
        union(parent, rank, a, b)

    groups = set()
    for i in range(1, N + 1):
        groups.add(find(parent, i))

    return len(groups)

# 입력 받기
N, K = map(int, input().split())
dislikes = []
for _ in range(K):
    a, b = map(int, input().split())
    dislikes.append((a, b))

# 최소 사진 찍는 횟수 계산
result = min_photos(N, dislikes)
print(result)