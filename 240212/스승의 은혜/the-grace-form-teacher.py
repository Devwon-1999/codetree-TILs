N, B = map(int, input().split())

present = []

for i in range(N):
    price, delivery = map(int, input().split())
    present.append([price, delivery])

present.sort()

cnt = 0
people = 0
for i in present:
    if cnt + sum(i) >= B:
            i[0] //= 2
            cnt += sum(i)
            break
    else:
        cnt += sum(i)
    people += 1

if B < sum(present[0]):
    print(0)
else:
    print(people + 1)