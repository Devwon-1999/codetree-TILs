#입력
N, M = map(int, input().split())
base = []
for i in range(N):
    string = input()

    temp = []
    for j in string:
        temp.append(j)
    base.append(temp)


for i in base:
    print(i)