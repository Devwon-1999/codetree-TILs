N = int(input())  #집의 수 N
first_peoples = list(map(int, input().split())) #사람들의 최초 위치를 저장하는 리스트
last_peoples = list(map(int, input().split()))  #사람들의 최종 위치를 저장하는 리스트

cnt = 0
for i in range(N):
    if first_peoples[i] == last_peoples[i]:
        continue
    else:
        while first_peoples[i] != last_peoples[i]:
            first_peoples[i] -= 1
            first_peoples[i + 1] += 1
            cnt += 1
print(cnt)