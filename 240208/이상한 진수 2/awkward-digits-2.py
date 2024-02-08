a = input()

if a == "0":
    print(1)

elif a == "1":
    print(0)
    
else:
    #입력된 문자열 형식의 a를 하나로 쪼갬
    a_list = [] 
    for i in a: 
        i = int(i)
        a_list.append(i)

    #제일 앞자리에 있는 0을 1로 변경
    for index, value in enumerate(a_list): 
        if value == 0:
            a_list[index] = 1
            break

    #변경된 이진수 정수화
    num = 0
    for i in a_list:
        i = int(i)
        num = num * 2 + i

    print(num)