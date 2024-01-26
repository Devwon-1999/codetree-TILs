n = int(input())

def isPrime(n):
    cnt = 0
    for i in range(1, n + 1):
        if n % i == 0:
            cnt += 1
    if cnt == 2:
        return True
    else:
        return False

if isPrime(n):
    print(n)
else:
    left_side = n
    right_side = n
    while True:
        
        left_side = left_side - 1
        right_side = right_side + 1
        
        if isPrime(left_side) and isPrime(right_side):
            print(left_side, right_side)
            break

        if isPrime(left_side):
            print(left_side)
            break
            
        if isPrime(right_side):
            print(right_side)
            break