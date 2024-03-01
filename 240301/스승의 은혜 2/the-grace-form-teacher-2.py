N, B = map(int, input().split()) #N명, B예산

price_List = []
for i in range(N):
    price = int(input())
    price_List.append(price)

price_List.sort()

print(price_List)