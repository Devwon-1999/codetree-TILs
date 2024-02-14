import sys
INT_MAX = sys.maxsize
min_val = INT_MAX

N = int(input()) # 방의 수 입력

bang = [] # 방별 수용 인원 수

for i in range(N): # 방별 수용 인원 수 입력
    temp = int(input())
    bang.append(temp)

#출발지 별 결과
for i in range(N):
    distance = 0
    for j in range(N): #현재 방의 위치부터 전체 방까지 반복
        index = (i + j) % N 
        distance += j * bang[index]
    min_val = min(min_val, distance)
    
print(min_val)