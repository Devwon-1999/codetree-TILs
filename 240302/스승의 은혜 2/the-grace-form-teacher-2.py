N, B = map(int, input().split()) #N명, B예산

price_List = []
for i in range(N):
    price = int(input())
    price_List.append(price)

price_List_cul = []
for i in range(N):
    temp = price_List.copy()
    temp[i] = temp[i] // 2
    price_List_cul.append(temp)

max_cnt = 0
for i in price_List_cul:
    i.sort()
    cnt = 0
    sum_price = 0
    for j in i:
        if B > sum_price + j:
            sum_price += j
            cnt += 1 
        else:
            break
    max_cnt = max(max_cnt, cnt)        

print(max_cnt)