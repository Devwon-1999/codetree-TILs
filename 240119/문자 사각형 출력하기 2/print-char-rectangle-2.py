n = int(input())

a = 65
trans1 = 2 * n - 1
trans2 = 1

for i in range(n):
    a = 65 + i
    if a > 90:
        a = 65
    for j in range(n):
        print(chr(a),end=" ")
        if j % 2 == 0:
            a += trans1
            if a > 90:
                a = a - 90 + 65 - 1
        else:
            a += trans2
            if a > 90:
                a = a - 90 + 65 - 1

    trans1 -= 2
    trans2 += 2
    print()