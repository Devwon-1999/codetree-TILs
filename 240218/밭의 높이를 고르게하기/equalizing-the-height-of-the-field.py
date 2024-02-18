N, H, T = map(int, input().split())
# N 밭 개수
# H 높이
# T 번
height_List = list(map(int, input().split()))


piece_List = []
for i in range(N - T + 1):
    temp = []
    for j in range(i, i + T):
        temp.append(height_List[j])
    piece_List.append(temp)

difference_List = []
for i in piece_List:
    temp = []
    for j in i:
        if j != H:
            temp.append(abs(j - H))
        else:
            temp.append(0)
    difference_List.append(temp)

min_val = 10000000000
for i in difference_List:
    min_val = min(sum(i), min_val)
print(min_val)