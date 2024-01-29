N = int(input())
base = []
for i in range(N):
    num = int(input())
    base.append(num)
    
cnt = 0
result = []
if N == 1:
    print(1)

else:
    for i in range(len(base)):
        if i + 1 >= len(base):
            break

        if base[i] > 0 and base[i+1] > 0:
            cnt += 1
        elif base[i] < 0 and base[i+1] < 0:
            cnt += 1
        else:
            result.append(cnt)
            cnt = 0
    result.append(cnt)


print(max(result) + 1)