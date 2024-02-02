N, K, P, T = map(int, input().split())
#N 명의 개발자
#K 번의 악수 동안만 전파
#P 최초 감염자
#T 반복
developer = [-1 for i in range(N)]
spread = [K for i in range(N)]

developer[P - 1] = 1
T_List = []

for i in range(T):
    t, x, y = map(int, input().split()) # t초에 x와 y가 악수를 함.
    
    T_List.append([t, x, y])

T_List.sort()

for i in T_List:
    if i[1] == P and spread[i[1] - 1] > 0:
        developer[i[2] - 1] = 1
        spread[i[1] - 1] -= 1
    else:
        continue

result = ""

for i in developer:
    if i == -1:
        result += "0"
    elif i == 1:
        result += "1"

print(result)