# N 입력 (1 ~ N의 자물쇠 수 범위)
N = int(input())

#열릴 수 있는 조합
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())
if N == 1:
    print(1)
else:
    #1 ~ N까지의 범위
    numList = []
    for i in range(1, N + 1):
        numList.append(i)

    # 각 조합((a1, b1, c1)과(a2, b2, c2))의 -2 ~ 2까지의 범위의 리스트
    a1_index = numList.index(a1)
    a1_List = []
    for i in range(a1_index - 2, a1_index + 2 + 1):
        if i <= len(numList):
            a1_List.append(numList[i])

    b1_index = numList.index(b1)
    b1_List = []
    for i in range(b1_index - 2, b1_index + 2 + 1):
        if i <= len(numList):
            b1_List.append(numList[i])

    c1_index = numList.index(c1)
    c1_List = []
    for i in range(c1_index - 2, c1_index + 2 + 1):
        if i <= len(numList):          
            c1_List.append(numList[i])

    a2_index = numList.index(a2)
    a2_List = []
    for i in range(a2_index - 2, a2_index + 2 + 1):
        if i <= len(numList):  
            a2_List.append(numList[i])

    b2_index = numList.index(b2)
    b2_List = []
    for i in range(b2_index - 2, b2_index + 2 + 1):
        if i <= len(numList):
            b2_List.append(numList[i])

    c2_index = numList.index(c2)
    c2_List = []
    for i in range(c2_index - 2, c2_index + 2 + 1):
        if i <= len(numList):        
            c2_List.append(numList[i])

    result = []
    for i in a1_List:
        for j in b1_List:
            for k in c1_List:
                if [i,j,k] not in result: #겹치는 경우를 제외하고 대입
                    result.append([i,j,k])

    for i in a2_List:
        for j in b2_List:
            for k in c2_List:
                if [i,j,k] not in result: #겹치는 경우를 제외하고 대입
                    result.append([i,j,k])

    print(len(result))