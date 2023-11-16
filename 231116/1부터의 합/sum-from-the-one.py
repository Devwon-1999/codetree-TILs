n = int(input())
prod = 0
for i in range(1, 101):
    prod += i 
    if prod >= n:
        
        prod -= i
        print(prod)
        break