n = int(input())
ran = n
alpha = 65
num = 1
for i in range(1, n + 1):
    for j in range(ran, 0, -1):
        if alpha > 90:
            alpha = 65
        print(chr(alpha), end = " ")
        alpha += 1
    for j in range(i):
        if num > 9:
            num = 1
        print(num, end = " ")
        num += 1
    ran -= 1   
     
    print()