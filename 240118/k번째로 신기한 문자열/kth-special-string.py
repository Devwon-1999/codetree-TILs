n, k, T = input().split()

n, k = int(n), int(k)

strList = []
result = []

for i in range(n):
    string = input()
    strList.append(string)

for i in strList:
    cnt = 0
    for j in range(len(T)):
        if i[j] != T[j]:
            break
        else:
            cnt += 1

    if cnt == len(T):
        result.append(i)
    else:
        continue

result.sort()

print(result[k - 1])