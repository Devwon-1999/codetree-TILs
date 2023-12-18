n = [0 for i in range(10)]
num1 = int(input())
num2 = int(input())
num3 = int(input())

mul = num1 * num2 * num3

while True:
    if mul > 0:
        temp = mul % 10
        n[temp] += 1
        mul = mul // 10
    else:
        break

for i in n:
    print(i)