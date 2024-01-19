n = int(input())

a = 65
trans1 = 2 * n - 1
trans2 = 1

for i in range(n):
    a = 65 + i
    if a > 90:
        a = 65 + a % 65
    if i % 2 == 0:
        for j in range(n):
            print(chr(a),end=" ")
            a += trans1
            temp = trans1
            trans1 = trans2
            trans2 = temp
            if a > 90:
                a = 65 + a % 65
    else:
        for j in range(n):
            print(chr(a),end=" ")
            a += n
            if a > 90:
                a = 65 + a % 65
    print()