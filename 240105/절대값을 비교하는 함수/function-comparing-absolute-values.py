def valueComparison(a, b):
    if a < 0:
        a *= -1
    if b < 0:
        b *= -1
    
    if a > b:
        print(a)
    else:
        print(b)

n = int(input())
for i in range(n):
    num1, num2 = map(int, input().split())
    valueComparison(num1, num2)