arr = []
index = 1
for i in range(3):
    a, b = map(int, input().split())
    arr.append(a)
    arr.append(b)
#arr[0]: 10L물통 arr[1]: 해당 물통의 초기값 3 
#arr[2]: 11L물통 arr[3]: 해당 물통의 초기값 4 
#arr[4]: 12L물통 arr[5]: 해당 물통의 초기값 5 
for i in range(100):
    # 10L 물통 -> 11L 물통
    if i % 3 == 0:
        if arr[2] >= arr[3] + arr[1]:        # 2번 물통의 물의 양과 1번 물통의 물의 양이 2번 물통의 총량을 넘지 않는다면    
            arr[3] = arr[3] + arr[1]         # 2번 물통은 가득 차게되고
            arr[1] = 0                       # 1번 물통은 비워지게 된다.

        else:                                # 만약 1번물통과 2번물통의 합친 양이 2번 물통의 총량을 넘는다면
            arr[1] = (arr[3] + arr[1]) - 11  # 1번 물통은 남은 양을 갖게 된다.
            arr[3] = 11                      # 2번 물통을 가득 채우고
        # print(arr[1], end=" ")
        # print(arr[3], end=" ")
        # print(arr[5], end=" ")

    # 11L 물통 -> 12L 물통
    if i % 3 == 1:
        if arr[4] >= arr[5] + arr[3]:        # 3번 물통의 물의 양과 2번 물통의 물의 양이 3번 물통의 총량을 넘지 않는다면
            arr[5] = arr[5] + arr[3]         # 3번 물통은 가득 차게되고
            arr[3] = 0                       # 2번 물통은 비워지게 된다.

        else:                                # 만약 2번물통과 3번물통의 물의 합친양이 3번 물통의 총량을 넘는다면
            arr[3] = (arr[5] + arr[3]) - 12  # 2번 물통은 남은 양을 갖게 된다.
            arr[5] = 12                      # 3번 물통의 물의양은 가득 차게되고
        # print(arr[1], end=" ")
        # print(arr[3], end=" ")
        # print(arr[5], end=" ") 
    if i % 3 == 2:
        # 12L 물통 -> 10L 물통
        if arr[0] >= arr[1] + arr[5]:        # 3번물통과 1번물통의 물의양의 합이 1번물통 총량을 넘지 않으면
            arr[1] = 10                      # 1번물통은 가득 차게되고 
            arr[5] = 0                       # 3번 물통은 비어지게 된다.

        else:                                # 3번물통과 1번물통의 물의양의 합이 1번물통 총량을 넘는다면
            arr[5] = (arr[5] + arr[1]) - 10  # 3번 물통은 둘의 합에서 1번 물통을 제외한 양(즉, 남은양을 갖게된다.)
            arr[1] = 10                      # 1물통은 가득차게 되고
        # print(arr[1], end=" ")
        # print(arr[3], end=" ")
        # print(arr[5], end=" ") 
        # print()


print(arr[1])
print(arr[3])
print(arr[5])