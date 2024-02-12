N, B = map(int, input().split())

presents = []

for i in range(N):
    price, delivery = map(int, input().split())
    presents.append((price, delivery))

presents.sort(key=lambda x: (x[0] + x[1], x[0]))  # 가격 + 배송비가 적은 순서대로 정렬

count = 0
for price, delivery in presents:
    if price <= B:
        B -= price
        count += 1
    elif price // 2 + delivery <= B:
        B -= price // 2 + delivery
        count += 1
    else:
        count = 0  # 예산 내에서 선물을 구매할 수 없는 경우 0으로 설정
        break

print(count)