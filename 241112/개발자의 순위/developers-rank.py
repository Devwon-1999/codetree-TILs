K, N = map(int, input().split())

answer = 0
ranking = []
for i in range(K):
    temp = list(map(int, input().split()))
    ranking.append(temp)
    

for i in range(1, N+1):
    for j in range(1, N+1):
        check = True
        if i == j: #같은 개발자일 경우 배제
            continue

        for dev in ranking:
            dev_i = dev.index(i)
            dev_j = dev.index(j)
        
            if dev_i > dev_j:
                check = False
        
        if check:
            answer += 1

print(answer)
