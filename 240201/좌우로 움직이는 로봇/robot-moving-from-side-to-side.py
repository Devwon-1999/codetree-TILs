#A와 B가 만났을때의 횟수 구하기
n, m = map(int, input().split())
#n A가 움직인 횟수, m B가 움직인 횟수
A_move = [] #A로봇의 동선
B_move = [] #B로봇의 동선
a_now = 0 #A로봇의 현재 위치
b_now = 0 #B로봇의 현재 위치

for i in range(n): #A
    t, d = input().split() # t 이동거리, d 방향
    t = int(t)
    
    if d == "L": # 좌측 이동시
        for i in range(t):
            a_now -= 1 
            A_move.append(a_now)
    elif d == "R": # 우측 이동시
        for i in range(t):
            a_now += 1
            A_move.append(a_now)


for i in range(m): #B
    t, d = input().split() # t 이동거리, d 방향
    t = int(t)

    if d == "L": # 좌측 이동시
        for i in range(t):
            b_now -= 1
            B_move.append(b_now)
    elif d == "R": # 우측 이동시
        for i in range(t):
            b_now += 1
            B_move.append(b_now)


loop = 0 #반복문을 돌릴 횟수
index = 0 #비교 후 더 길게 이동한 로봇과 그렇지 않은 로봇의 비교를 위한 인덱스
end = 0 #마지막 인덱스
if len(A_move) >= len(B_move):
    loop = len(B_move)
    end = len(A_move)
elif len(A_move) < len(B_move):
    loop = len(A_move)
    end = len(B_move)
cnt = 0 #만나는 횟수


for i in range(loop):
    if i + 1 == loop:
        break
        
    if A_move[i] != B_move[i] and A_move[i+1] == B_move[i+1]:
        cnt += 1
    index += 1

if len(A_move) >= len(B_move):
    for i in range(index, end):
        if B_move[index-1] == A_move[i-1] and B_move[index] == A_move[i]:
            cnt += 1
elif len(A_move) < len(B_move):
    for i in range(index, end):
        if A_move[index - 1] == B_move[i - 1] and A_move[index] == B_move[i]:
            cnt += 1


print(cnt)