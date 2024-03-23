N = int(input())

base = []
for i in range(N):
    num, cnt1, cnt2 = map(int, input().split())
    base.append([num, cnt1, cnt2])

cnt = 0
for num100 in range(1, 10): # 백의자리
    for num10 in range(1, 10): # 십의자리
        for num1 in range(1, 10): # 일의자리
            if num100 == num10 or num10 == num1 or num100 == num1: # 서로 다른 3개의 수로 구성되어 있기 때문에
                continue                                           # 한 자리 수라도 다른 경우를 고려할 필요가 없다.
            
            answer = True
            for num, cnt1, cnt2 in base: 
                num_100 = num // 100    #백의자리
                num_10 = num // 10 % 10 #십의자리
                num_1 = num % 10        #일의자리

                cnt_1 = 0
                cnt_2 = 0
                #각각의 경우에 따라서 같을 경우 새로운 카운팅을 해준다
                if num_100 == num100:   
                    cnt_1 += 1
                if num_10 == num10:
                    cnt_1 += 1
                if num_1 == num1:
                    cnt_1 += 1
                if num_100 == num10 or num_100 == num1:
                    cnt_2 += 1
                if num_10 == num100 or num_10 == num1:
                    cnt_2 += 1
                if num_1 == num100 or num_1 == num10:
                    cnt_2 += 1

                #카운팅과 카운팅이 같은경우는 정답이 될 수 있는 경우로 판단한다
                #카운팅과 카운팅이 다른경우는 정답이 아니다.
                if cnt1 != cnt_1 or cnt2 != cnt_2:
                    answer = False
                    break
            if answer:
                cnt += 1

print(cnt)