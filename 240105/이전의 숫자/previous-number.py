n = int(input())
numList = list(map(int, input().split()))

result = 0

for i in numList[-6:-1]:
    result += i

print(result)