N = int(input()) # 방의 수 입력

bang = [] # 방별 수용 인원 수

for i in range(N): # 방별 수용 인원 수 입력
    temp = int(input())
    bang.append(temp)



min_val = 1000000
move_people = 0
for i in range(N):
    current = bang[i]
    total_people = sum(bang) # 전체 인원
    for j in range(N):
        j = (i + j) % 5 #현재 방의 위치부터 전체 방까지 반복
        total_people -= current
        current = bang[j]
        move_people += total_people
    min_val = min(min_val, move_people)

print(min_val)