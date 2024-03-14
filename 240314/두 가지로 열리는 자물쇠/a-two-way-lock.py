#다른 방법으로의 풀이
N = int(input()) # 최대 자물쇠 숫자
one = list(map(int, input().split())) # 첫 번째 조합
two = list(map(int, input().split())) # 두 번째 조합

N_List = [i for i in range(1, N + 1)] #자물쇠의 숫자 범위

#첫번째 자리와 조합의 거리가 2 이내인 경우

# 각 자릿수 별 인덱스
one_index_1 = N_List.index(one[0])
two_index_1 = N_List.index(one[1])
three_index_1 = N_List.index(one[2])

# 각 자릿수 별 범위
one_1 = [] #첫 번째 수의 -2 ~ + 2 범위
one_2 = [] #두 번째 수의 -2 ~ + 2 범위
one_3 = [] #세 번째 수의 -2 ~ + 2 범위

# 각 자릿수 별 범위 대입
for i in range(one_index_1 - 2, one_index_1 + 3):
    one_1.append(N_List[i])
for i in range(two_index_1 - 2, two_index_1 + 3):
    one_2.append(N_List[i])
for i in range(three_index_1 - 2, three_index_1 + 3):
    one_3.append(N_List[i])   


#두번째 자리와 조합의 거리가 2 이내인 경우
# 각 자릿수 별 인덱스
one_index_2 = N_List.index(two[0])
two_index_2 = N_List.index(two[1])
three_index_2 = N_List.index(two[2])

# 각 자릿수 별 범위
two_1 = [] #첫 번째 수의 -2 ~ + 2 범위
two_2 = [] #두 번째 수의 -2 ~ + 2 범위
two_3 = [] #세 번째 수의 -2 ~ + 2 범위

# 각 자릿수 별 범위 대입
for i in range(one_index_2 - 2, one_index_2 + 3):
    two_1.append(N_List[i])
for i in range(two_index_2 - 2, two_index_2 + 3):
    two_2.append(N_List[i])
for i in range(three_index_2 - 2, three_index_2 + 3):
    two_3.append(N_List[i])   


#첫번째 혹은 두번째를 만족할 경우 잠물쇠는 열리게 된다.
#이 경우의 가짓수를 구해서 출력하는 프로그램을 작성

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