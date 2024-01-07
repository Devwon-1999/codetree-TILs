n = int(input())

numList = list(map(int, input().split()))
result = 0
cnt = 0
for i in numList:
    
    if result > 200:
        print(result)
        break
    result += i
    cnt += 1
print("%.1f" % (result / cnt))