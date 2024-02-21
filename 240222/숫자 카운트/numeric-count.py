N = int(input())
base = [str(i) for i in range(100, 1000)]

answer = []
for i in range(N):
    num, cnt1, cnt2 = map(int, input().split())
    #cnt1 num중 한자리가 동일한 위치
    #cnt2 num중 한자리가 다른 위치
    num = str(num)

    if cnt1 == 0 and cnt2 == 0:
        for i in base:
            if num[0] in i or num[1] in i or num[2] in i:
                answer.append(i)

    elif cnt1 == 1 and cnt2 == 0:

    elif cnt1 == 0 and cnt2 == 1

    elif cnt1 == 1 and cnt1 == 1:
    
print(len(answer))