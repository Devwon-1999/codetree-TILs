#크기, 출력형식 
size, order = map(int, input().split())

#크기만큼의 배열 초기화
result = [[1]*i for i in range(1, size + 1)]

#배열을 파스칼 삼각형으로
for i in range(size):
    for j in range(1, i):
        result[i][j] = result[i-1][j-1] + result[i-1][j]


if order == 1: # 1형식 출력 결과
    for i in range(size):
        for j in range(i+1):
            print(result[i][j], end=" ")
        print()

elif order == 2: # 2형식 출력 결과
    cnt = 1
    for i in range(size - 1, -1, -1):
        
        for j in range(i + 1):
            print(result[i][j], end=" ")
        print()
        print(" " * cnt, end = "")
        cnt += 1
  
elif order == 3: # 3형식 출력 결과
    x = size
    y = size
    for i in range(size):
        x = size 
        y -= 1
        for j in range(i+1):
            x -= 1
            print(result[x][y], end=" ")
        print()