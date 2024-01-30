#A와 B가 만났을때의 횟수 구하기
n, m = map(int, input().split())
#n A가 움직인 횟수
#m B가 움직인 횟수
A_move = []
B_move = []
a_now = 0
b_now = 0

for i in range(n): #A
    t, d = input().split() # t 이동거리, d 방향
    t = int(t)
    
    if d == "L":
        for i in range(t):
            a_now -= 1
            A_move.append(a_now)
    elif d == "R":
        for i in range(t):
            a_now += 1
            A_move.append(a_now)


for i in range(m): #B
    t, d = input().split() # t 이동거리, d 방향
    t = int(t)

    if d == "L":
        for i in range(t):
            b_now -= 1
            B_move.append(b_now)
    elif d == "R":
        for i in range(t):
            b_now += 1
            B_move.append(b_now)


loop = 0 #반복문을 돌릴 횟수
if len(A_move) >= len(B_move):
    loop = len(B_move)

elif len(A_move) < len(B_move):
    loop = len(A_move)

cnt = 0 #만나는 횟수
for i in range(loop):
    if i + 1 == loop:
        break

    if A_move[i] != B_move[i] and A_move[i+1] == B_move[i+1]:
        cnt += 1
    
print(cnt + 1)