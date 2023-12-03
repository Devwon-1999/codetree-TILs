n = int(input())
prices = list(map(int, input().split()))


max_profit = 0
min_price = prices[0]


for i in range(1, n):
    current_price = prices[i]
    current_profit = current_price - min_price

    if current_profit > max_profit:
        max_profit = current_profit

    if current_price < min_price:
        min_price = current_price


print(max_profit)