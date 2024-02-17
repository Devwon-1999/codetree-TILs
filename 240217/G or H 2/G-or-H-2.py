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

for i in range(start, end):
    tempList = []
    for j in range(i, end):
        temp = []
        for k in range(i, j + 1):
            temp.append(base[k])

    if len(temp) % 2 == 0:
        H_cnt = 0
        G_cnt = 0
        for i in temp:
            if i == "H":
                H_cnt += 1
            elif i == "G":
                G_cnt += 1
        if H_cnt % 2 == 0 and G_cnt % 2 == 0:
            tempList.append(temp)
    else:
        continue
        
            
print(tempList)