N, H, T = map(int, input().split())
# N 밭 개수
# H 높이
# T 번
height_List = list(map(int, input().split()))

for i in range(N - T + 1):
    for j in range(i, i + T):
        print(i, j)
    print()