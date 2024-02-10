N = int(input()) # 방의 수 입력

bang = [] # 방별 수용 인원 수

for i in range(N): # 방별 수용 인원 수 입력
    temp = int(input())
    bang.append(temp)

total_people = sum(bang) # 전체 인원

moveList = []
for i in range(N):
    total_people -= bang[i]
    move = 0
    for j in range(N):
        total_people -= bang[j]
        move += bang[j]
    moveList.append(move)

print(moveList)