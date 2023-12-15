A = input()
B = input()

cnt = 0

for i in range(len(A)):
    if cnt == len(A):
        print(-1)
        break
    if A == B:
        break
    else:
        cnt += 1
        A = A[-1] + A[0:len(A)-1]
    
print(cnt)