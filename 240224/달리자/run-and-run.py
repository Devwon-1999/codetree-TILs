N = int(input())  #집의 수 N
first_peoples = list(map(int, input().split())) #사람들의 최초 위치를 저장하는 리스트
last_peoples = list(map(int, input().split()))  #사람들의 최종 위치를 저장하는 리스트

cnt = 0 #정답을 저장할 변수
for i in range(N): #N회 반복
    if first_peoples[i] == last_peoples[i]: #만약 first리스트의 i번째 집과 last리스트의 i번째집에 있는 사람수가 같다면
        continue                            #따로 건들일 것 없이 다음으로 이동
    else:
        while first_peoples[i] != last_peoples[i]: # 각각의 같은 번째수의 집에 사람의 수가 다르다면
            first_peoples[i] -= 1                  # 해당 집의 사람을 감소시키고
            first_peoples[i + 1] += 1              # 다음 집의 사람을 증가시킨다
            cnt += 1                               # 위의 경우 이동을 했다고 판단하며 1을 증가시킨다
print(cnt) #정답 출력