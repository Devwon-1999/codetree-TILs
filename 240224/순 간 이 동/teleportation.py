A, B, x, y = map(int, input().split())

#A부터 B까지 이동
#x, y 쌍방향 순간이동 가능

#a,b와 x,y가 전혀 관련 없는경우
if B < min(x, y):
    cnt = 0
    for i in range(A, B + 1):
        cnt += 1
    print(cnt)

#a,b 사이에 x, y의 최소 값이 있는 경우
elif A <= min(x, y) <= B:
    cnt = 0
    for i in range(A, min(x, y)):
        cnt += 1
    print(cnt)

#a,b 사이에 x, y의 최대 값이 있는 경우
# elif A <= max(x, y) <= B: