#입력
N, M = map(int, input().split())
base = []
for i in range(N):
    string = input()

    temp = []
    for j in string:
        temp.append(j)
    base.append(temp)

def in_range(x, y):
    return 0 <= x and x < M and 0 <= y and y < N
    
dxys = [
    #        가로                  세로                     대각선
    [[0, 1, 2],[0, 0, 0]], [[0, 0, 0],[0, 1, 2]], [[0, 1, 2],[0, 1, 2]], 
    [[0, -1, -2],[0, 0, 0]], [[0, 0, 0],[0, -1, -2]], [[0, -1, -2],[0, -1, -2]]
]
for i in range(N):
    for j in range(M):
        if base[i][j] == "L":
            print(base[i][j], end = " ")
            for dxs, dys in dxys:
                for dx, dy in zip(dxs, dys):
                    if in_range(i + dx, i + dy) and base[dx][dy] == "E":
                        print(base[dx][dy], end = " ")
            print()