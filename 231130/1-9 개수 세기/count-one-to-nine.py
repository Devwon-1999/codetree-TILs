n = int(input())
inputNum = list(map(int, input().split()))
resultArr = [0 for _ in range(9)]

for i in inputNum:
        resultArr[i - 1] += 1
    

for i in resultArr:
    print(i)