inputNum = list(map(int, input().split()))

resultArr = [0 for _ in range(6)]
index = 1
for i in inputNum:
        resultArr[i - 1] += 1
    

for i in resultArr:
    print(f"{index} - {i}")
    index += 1