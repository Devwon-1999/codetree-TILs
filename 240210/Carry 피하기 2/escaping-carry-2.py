N = int(input()) #입력될 숫자의 갯수

numList = [] #입력된 숫자 리스트
numList_1 = [] #숫자 리스트의 1의자리만 모은 리스트
numList_2 = [] #숫자 리스트의 10의자리만 모은 리스트
numList_3 = [] #숫자 리스트의 100의자리만 모은 리스트
numList_4 = [] #숫자 리스트의 1000의자리만 모은 리스트

#입력
for i in range(N):
    temp = int(input())
    numList.append(temp)

#숫자의 자릿수별 리스트 대입
for i in numList:
    numList_1.append(i % 10)
    numList_2.append((i % 100) // 10)
    numList_3.append((i % 1000) // 100)
    numList_4.append((i % 10000) // 1000)

#각 자리수가 모두 10을 넘지 않는 경우(carry가 발생하지 않는 경우)의 인덱스 찾기
checked_case = []
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if numList_1[i] + numList_1[j] + numList_1[k] < 10 and numList_2[i] + numList_2[j] + numList_2[k] < 10 and numList_3[i] + numList_3[j] + numList_3[k] < 10 and numList_4[i] + numList_4[j] + numList_4[k] < 10:
                checked_case.append([i, j, k])


#위의 경우에 만족하면서 최댓값 찾기
max_Value = 0

for i, j, k in checked_case:
    max_Value = max(max_Value, numList[i] + numList[j] + numList[k])

#경우가 있다면 경우, 없다면 -1 출력
if max_Value:
    print(max_Value)
else:
    print(-1)