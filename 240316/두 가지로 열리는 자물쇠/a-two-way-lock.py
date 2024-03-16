#다른 방법으로의 풀이
N = int(input()) # 최대 자물쇠 숫자
one = list(map(int, input().split())) # 첫 번째 조합
two = list(map(int, input().split())) # 두 번째 조합

N_List = [i for i in range(1, N + 1)] #자물쇠의 숫자 범위

def return_range(arr):
    index_1 = N_List.index(arr[0])
    index_2 = N_List.index(arr[1])
    index_3 = N_List.index(arr[2])

    one = []
    two = []
    three = []

    for i in range(index_1 - 2, index_1 + 3):
        if is_in_range(i):
            one.append(N_List[i])
        elif i == len(N_List):
            a = 0
            one.append(N_List[a])
        elif i > len(N_List):
            a = i - len(N_List)
            one.append(N_List[a])
    for i in range(index_2 - 2, index_2 + 3):
        if is_in_range(i):
            two.append(N_List[i])
        elif i == len(N_List):
            a = 0
            two.append(N_List[a])
        elif i > len(N_List):
            a = i - len(N_List)
            two.append(N_List[a])
    for i in range(index_3 - 2, index_3 + 3):
        if is_in_range(i):
            three.append(N_List[i])
        elif i == len(N_List):
            a = 0
            three.append(N_List[a])
        elif i > len(N_List):
            a = i - len(N_List)
            three.append(N_List[a])
    return one, two, three


def is_in_range(i):
    if i in range(-len(N_List), len(N_List)):
        return True
    else:
        return False


one_1, one_2, one_3 = return_range(one)
two_1, two_2, two_3 = return_range(two) 


result = [] #정답

for i in one_1:
    for j in one_2:
        for k in one_3:
            if [i, j, k] not in result:
                result.append([i, j ,k])       

for i in two_1:
    for j in two_2:
        for k in two_3:
            if [i, j, k] not in result:
                result.append([i, j ,k])

print(len(result))