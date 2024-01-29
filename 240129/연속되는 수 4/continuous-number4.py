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

        if base[i] < base[i+1]:
            cnt += 1

        else:
            result.append(cnt)
            cnt = 0
    result.append(cnt)

if result:
    print(max(result) + 1)