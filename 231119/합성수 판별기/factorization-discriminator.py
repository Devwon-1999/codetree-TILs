n = int(input())
nothapsungsu = 0
if n >= 1:
    for i in range(1, n+1):
        if n % i == 0:
            nothapsungsu += 1
else:
    print("N")

if nothapsungsu > 2:
    print("C")
else:
    print("N")