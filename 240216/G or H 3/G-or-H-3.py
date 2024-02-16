N, K = map(int, input().split())
#N명의 사람, K의 사진크기

base = [0 for i in range(10001)] #총 100개의 위치

for i in range(N): 
    place, alpha = input().split() #위치와 알파벳
    place = int(place)
    base[place] = alpha

result = []
for i in range(10001 - K):
    temp = 0
    for j in range(i, i + K + 1):
        if base[j] == "G":
            temp += 1
        elif base[j] == "H":
            temp += 2
    result.append(temp)
print(max(result))