N, M, K = map(int, input().split()) #입력

base = [[0] * (M * K)] * (N * K) # 결과 값을 출력할 리스트
tempList = [] # 입력된 문자를 입시로 저장하는 리스트

for i in range(N): #입력
    temp = list(input())
    tempList.append(temp)


for n in range(N):
    for k in range(K):
        for m in range(M):
            print(tempList[n][m]*K, end="")        
        print()