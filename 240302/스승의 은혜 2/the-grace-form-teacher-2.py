N, B = map(int, input().split()) #N명, B예산

price_List = []
for i in range(N):
    price = int(input())
    price_List.append(price)

price_List.sort()

sum_price = 0
cnt = 0
for i in price_List:
    if B > sum_price:
        sum_price += i
        cnt += 1
if B >= sum_price + price_List[cnt] // 2:
    sum_price + price_List[cnt] // 2
print(cnt)