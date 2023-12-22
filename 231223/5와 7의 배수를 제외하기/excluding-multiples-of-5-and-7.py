n = int(input())

numList = list(map(int, input().split()))
result = []
for i in numList:
    if i % 7 != 0 and i % 5 != 0:
        result.append(i)

print(sum(result))
print("%.1f" % (sum(result)/len(result)))