N, M = map(int, input().split())
now_A = 500
A = []
now_B = 500
B = []

for i in range(N): # A 
    order, length = input().split()
    length = int(length)
    if order == "R":
        for i in range(length):
            now_A += 1
            A.append(now_A)
    elif order == "L":
        for i in range(length):
            now_A -= 1
            A.append(now_A)
            

for i in range(M): # B 
    order, length = input().split()
    length = int(length)
    if order == "R":
        for i in range(length):
                now_B += 1
                B.append(now_B)
    elif order == "L":
        for i in range(length):
            now_B -= 1
            B.append(now_B)
result = 0
for i in range(len(A)):
    result += 1
    if A[i] == B[i]:
        print(result)
        break