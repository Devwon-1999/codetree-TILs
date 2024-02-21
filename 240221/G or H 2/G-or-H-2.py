N = int(input())
base = [0 for i in range(100)]
placeList = []
for i in range(N):
    place, alpha = input().split()
    place = int(place) - 1

    base[place] = alpha
    placeList.append(place)

placeList.sort()
start = placeList[0]
end = placeList[-1] + 1
tempList = []
for i in range(start, end):
    
    for j in range(i, end):
        temp = []
        for k in range(i, j + 1):
            temp.append(base[k])
        
        if len(temp) % 2 == 0 or len(temp) % 2 == 1:
            H_cnt = 0
            G_cnt = 0
            for a in temp:
                if a == "H":
                    H_cnt += 1
                elif a == "G":
                    G_cnt += 1
            if H_cnt == 0:
                tempList.append(temp)
            if G_cnt == 0:
                tempList.append(temp)
            if H_cnt == G_cnt:
                tempList.append(temp)
            else:
                continue
        else:
            continue

answer = []
for i in tempList:
    if i[0] != 0:
        answer.append(i)

answer2 = []
for i in answer:
    i.reverse()
    if i[0] != 0:
        answer2.append(i)
max_val = 0
for i in answer2:
    max_val = max(max_val, len(i) - 1)

print(max_val)