gam1, tem1 = input().split()
gam2, tem2 = input().split()
gam3, tem3 = input().split()

tem1 = int(tem1)
tem2 = int(tem2)
tem3 = int(tem3)

A = 0
B = 0
C = 0
D = 0

if gam1 == "Y" and tem1 >= 37:
    A += 1
elif gam1 == "N" and tem1 >= 37:
    B += 1
elif gam1 == "Y" and tem1 <= 37:
    C += 1
elif gam1 == "N" and tem1 <= 37:
    D += 1

if gam2 == "Y" and tem2 >= 37:
    A += 1
elif gam2 == "N" and tem2 >= 37:
    B += 1
elif gam2 == "Y" and tem2 <= 37:
    C += 1
elif gam2 == "N" and tem2 <= 37:
    D += 1

if gam3 == "Y" and tem3 >= 37:
    A += 1
elif gam3 == "N" and tem3 >= 37:
    B += 1
elif gam3 == "Y" and tem3 <= 37:
    C += 1
elif gam3 == "N" and tem3 <= 37:
    D += 1

if A >= 2:
    print("E")
else:
    print("N")