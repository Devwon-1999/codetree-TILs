n = int(input())
num = 0
alpha = 65
for i in range(n + 1):
    for j in range(n - i):
        print(chr(alpha), end = " ")
        alpha += 1
        if alpha > 90:
            alpha = 65
            
    for j in range(i):
        print(num, end = " ")
        num += 1
        if num > 9:
            num = 0
    print()