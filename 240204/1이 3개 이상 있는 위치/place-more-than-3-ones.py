n = int(input()) 
base = [] # 입력된 전체 좌표

def in_range(x, y): # 좌표가 범위 내에 있는지 확인하는 함수
    return 0 <= x and x < n and 0 <= y and y < n


for i in range(n): # 입력 값을 좌표화
    temp = list(map(int, input().split()))
    base.append(temp)

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0] #좌표 기준 북 동 남 서의 좌표
result = [] #결과 값(좌표)을 담을 리스트

for y in range(n): #base의 모든 좌표를 대상
    for x in range(n): #base의 모든 좌표를 대상
        cnt = 0
        for dx, dy in zip(dxs, dys): #좌표기준 동서남북의 좌표에 대해서
            nx, ny = x + dx, y + dy
            if in_range(nx, ny) and base[nx][ny] == 1: #좌표의 유효성, 좌표 값이 1인경우를 확인 후
                cnt += 1
        if cnt >= 3: # 좌표값이 1인 경우가 3번 이상이라면
            result.append([x + 1, y + 1]) # 해당 좌표를 결과 값에 대입

print(len(result)) #결과 출력