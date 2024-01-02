def printSquare(n):
    cnt = 1
    temp = 1
    for i in range(n):
        
        for j in range(n):
            print(cnt, end = " ")
            cnt += n
        print()
        temp += 1
        cnt = temp

n = int(input())

printSquare(n)