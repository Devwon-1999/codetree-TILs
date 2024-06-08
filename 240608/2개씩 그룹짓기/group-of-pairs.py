n = int(input())

numList = list(map(int, input().split()))
div_list = []
result_list = []
numList.sort()

for i in range(n):
    minnum = numList.pop(0)
    maxnum = numList.pop(len(numList) - 1)

    div_list.append([minnum, maxnum])

for i in div_list:
    temp = 0
    for j in i:
        temp += j
    result_list.append(temp)

print(max(result_list))