Developer = list(map(int, input().split()))

result = []
for a in range(len(Developer)):
    for b in range(len(Developer)):
        for c in range(len(Developer)):
            for d in range(len(Developer)):
                for e in range(len(Developer)):
                    if a != b and a != c and a != d and a != e: # 각각의
                        if b != c and b != d and b != e:        # 개발자가
                            if c != d and c != e:               # 뽑힌
                                if d != e:                      # 경우
                                    if Developer[a] + Developer[b] != Developer[c] + Developer[d] and Developer[a] + Developer[b] != Developer[e] and Developer[c] + Developer[d] != Developer[e]: #모든 능력치가 서로 다른 경우
                                        temp = [Developer[a] + Developer[b], Developer[c] + Developer[d], Developer[e]] #3개의 팀의 능력치 중
                                        result.append(max(temp) - min(temp)) #최대의 값과 최소의 값의 차가 가장 낮은경우 result 배열에 대입

print(min(result))