N, M = map(int, input().split()) #입력

#변수 및 리스트 선언
A_move = []
B_move = []
Amove = 0
Bmove = 0

#A와 B의 시간비례 거리 리스트 추가
for i in range(N): # A
    v, t = map(int, input().split())
    for i in range(t):
        Amove += v
        A_move.append(Amove)
for i in range(M): # B
    v, t = map(int, input().split())
    for i in range(t):
        Bmove += v
        B_move.append(Bmove)

result = []
#시간대별 거리 측정 후 result 리스트에 추가
for i in range(len(A_move)):
    if A_move[i] == B_move[i]:
        result.append(["A, B"])
    elif A_move[i] > B_move[i]:
        result.append(["A"])
    elif A_move[i] < B_move[i]:
        result.append(["B"])

answer = 0
#바뀐 횟수 출력
for i in range(len(result)):
    if i + 1 == len(result):
        break
    if result[i] != result[i + 1]:
        answer += 1

print(answer + 1)