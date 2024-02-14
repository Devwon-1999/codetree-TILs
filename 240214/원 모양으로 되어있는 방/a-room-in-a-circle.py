N = int(input()) # 방의 수 입력

bang = [] # 방별 수용 인원 수

for i in range(N): # 방별 수용 인원 수 입력
    temp = int(input())
    bang.append(temp)

min_val = 1000000

for i in range(N):
    distance = 0
    for j in range(N): #현재 방의 위치부터 전체 방까지 반복
        index = (i + j) % N 
        distance += j * bang[index]
    min_val = min(min_val, distance)
    
print(min_val)