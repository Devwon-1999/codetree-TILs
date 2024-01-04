A = input()
B = input()

cnt = 0

for i in range(len(A)):
    A = A[-1:] + A[0:len(A) - 1]
    cnt += 1
    if A == B:
        print(cnt)
        break
    
if A != B:
    print(-1)