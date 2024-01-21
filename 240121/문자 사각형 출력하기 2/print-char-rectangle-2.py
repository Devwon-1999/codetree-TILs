n = int(input())

a = 65
trans1 = 2 * n - 1
trans2 = 1

for i in range(n):
    a = 65 + i
    if a > 90:
        a -= 26
    for j in range(n):
        print(chr(a), end=" ")

        if j % 2 == 0:
            a += trans1
            if a > 90:
                temp = a % 90
                a = (a % 90) % 26 + 65 
                if temp >= 25:
                    a += 1
                else:
                    a -= 1
        else:
            a += trans2
            if a > 90:
                temp = a % 90
                a = (a % 90) % 26 + 65 
                if temp >= 25:
                    a += 1
                else:
                    a -= 1

    trans1 -= 2
    trans2 += 2
    print()