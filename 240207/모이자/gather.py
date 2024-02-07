n = int(input())
numList = list(map(int, input().split()))

result = []

for i in range(n):
    target = 0
    for j in range(n):
        if j != i:
            target += int(numList[j]) * abs(i - j)
    result.append(target)

print(min(result))





# result = []
# for i in range(len(home)):
#     k = 0
#     for j in range(len(home)):
#         if j != i:
#             k += int(home[j]) * abs(j - i)
#     result.append(k)
# print(min(result))