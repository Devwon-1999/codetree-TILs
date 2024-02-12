N, B = map(int, input().split())

presents = []

for i in range(N):
    price, delivery = map(int, input().split())
    presents.append((price, delivery))

presents.sort(key=lambda x: (x[0] + x[1], x[0]))  # 가격 + 배송비가 적은 순서대로 정렬

count = 0
coupon_used = False  # 쿠폰 사용 여부를 나타내는 변수 추가
for price, delivery in presents:
    if price <= B:
        B -= price
        count += 1
    elif not coupon_used and price // 2 + delivery <= B:  # 쿠폰을 사용하여 예산 내에서 선물을 구매하는 경우
        B -= price // 2 + delivery
        count += 1
        coupon_used = True  # 쿠폰을 사용했으므로 True로 설정
    else:
        break

print(count)