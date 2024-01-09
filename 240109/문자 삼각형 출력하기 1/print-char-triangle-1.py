n = int(input())
cnt = 65
for i in range(1, n+1):
    for j in range(n - i):
        print(" ", end= " ")
        
        
    for j in range(1, i+1):
        print(chr(cnt), end= " ")    
        cnt = cnt + (n - j)
        if cnt == 91:
            cnt = 65
        
    cnt = 65 + i
    if cnt >= 91:
            cnt = 65 + (cnt % 65)
    print()