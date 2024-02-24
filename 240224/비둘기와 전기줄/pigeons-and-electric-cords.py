N = int(input()) # 비둘기가 총 이동했던 경우 N번 입력

place = [-1 for i in range(11)] # 비둘기들의 현재 위치
cnt = 0 #정답을 기록할 cnt(카운트, 움직인 횟수 계산시 사용할) 변수

for i in range(N): #반복문 N번 반복
    a, b = map(int, input().split()) #a 비둘기, b 위치
    if place[a - 1] == -1:
        place[a - 1] = b
    elif place[a - 1] == 1:
        if b == 0:
            cnt += 1
            place[a - 1] = 0
    elif place[a - 1] == 0:
        if b == 1:
            cnt += 1
            place[a - 1] = 1

print(cnt)