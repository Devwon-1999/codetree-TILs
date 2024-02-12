N, B = map(int, input().split())

presents = []

for i in range(N):
    price, delivery = map(int, input().split())
    presents.append((price + delivery, price))  # 선물 가격과 배송비를 더한 값과 선물 가격만 저장

presents.sort()  # 가격 + 배송비가 적은 순서대로 정렬

count = 0
for price_plus_delivery, price in presents:
    if price <= B:  # 현재 학생의 선물 가격이 예산 내에 있는 경우
        B -= price  # 예산에서 선물 가격을 차감
        count += 1  # 선물을 준 학생 수 증가
    elif B >= price // 2:  # 절반 가격으로 선물을 구매할 수 있는 경우
        B -= price // 2  # 절반 가격을 지불하고 선물을 줌
        count += 1  # 선물을 준 학생 수 증가
        break  # 더 이상 선물을 줄 수 없음
    else:
        break  # 선물을 구매할 예산이 부족한 경우 루프 탈출

print(count)