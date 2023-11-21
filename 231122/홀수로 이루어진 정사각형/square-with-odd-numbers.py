n = int(input())

for i in range(1, n*2+1, 2):
    for j in range(1, n*2+1, 2):
        print(f"{j+i+9}",end=' ')
    print()