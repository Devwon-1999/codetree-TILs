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

# 두 로봇의 움직임의 횟수가 다를경우 한가지 로봇은 한곳에 머무른다.
# 두 로봇의 움직임 중 더 적게 움직인 로봇의 동선 (A_move, B_move) 리스트에 가만히 머무르는 것을 추가한다.
if len(A_move) > len(B_move):
    difference = len(A_move) - len(B_move)
    for i in range(difference):
        B_move.append(B_move[-1])
elif len(A_move) < len(B_move):
    difference = len(B_move) - len(A_move)
    for i in range(difference):
        A_move.append(A_move[-1])

result = 0
# 이전에는 다른 칸에 있었지만 현재는 같은 칸에 있는 경우를 샌다
for i in range(len(A_move) - 1):
    if A_move[i] != B_move[i] and A_move[i + 1] == B_move[i + 1]:
        result += 1

print(result)