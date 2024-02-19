N = int(input())
a, b, c = map(int, input().split())

a_List = [a - 2, a - 1, a, a + 1, a + 2]
b_List = [b - 2, b - 1, b, b + 1, b + 2]
c_List = [c - 2, c - 1, c, c + 1, c + 2]

cnt = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if i not in a_List and j not in b_List and k not in c_List:
                cnt += 1

print(N**3 - cnt)