# 색종이의 갯수
n = int(input())

# 격자 초기화
grid = [[0] * 501 for _ in range(501)]

# 색종이의 좌표를 받아 격자에 표시
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            grid[i][j] += 1

# 파란 영역의 넓이 계산
blue_area = 0
for i in range(501):
    for j in range(501):
        if grid[i][j] > 0:
            blue_area += 1

# 결과 출력
print(blue_area)