N, B = map(int, input().split())

present = []

for i in range(N):
    price, delivery = map(int, input().split())
    present.append([price, delivery])

present.sort()

total_price = 0
people = 0
for i in present:
    if total_price + i[0] >= B:
        i[0] //= 2  # 쿠폰 사용
        total_price += i[0]
        break
    else:
        total_price += i[0]
        people += 1

if B < present[0][0]:  
    print(0)
else:
    print(people + 1)