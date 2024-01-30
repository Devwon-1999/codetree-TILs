#문제 서로 역전을 몇번하는지 계산
N, M = map(int, input().split()) #N A의 이동, M B의 이동
A_move = []
B_move = []

for i in range(N):
    v, t = map(int, input().split()) #v속도 t시간
    for i in range(t):
        A_move.append(v)
for i in range(M):
    v, t = map(int, input().split()) #v속도 t시간
    for i in range(t):
        B_move.append(v)


a_length = 0
b_length = 0
result = []

for i in range(len(A_move)): #시간대별 길이를 계산, result에 앞서있는 것을 대입
    a_length += A_move[i]
    b_length += B_move[i]

    if a_length > b_length:
        result.append("a")
    elif a_length < b_length:
        result.append("b")


cnt = 0

for i in range(len(result)): #result에서 앞과 뒤가 다른(역전) 경우일 때 마다 cnt변수 += 1
    if i + 1 == len(result):
        break
    if result[i] != result[i + 1]:
        cnt += 1
    

print(cnt)