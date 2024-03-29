Developer = list(map(int, input().split()))

result = []
for a in range(len(Developer)):
    for b in range(len(Developer)):
        if b == a:
            continue
        for c in range(len(Developer)):
            if c == a or c == b:
                continue
            for d in range(len(Developer)):
                if d == a or d == b or d == c:
                    continue
                for e in range(len(Developer)):
                    if e == a or e == b or e == c or e == d:
                        continue
                    if Developer[a] + Developer[b] != Developer[c] + Developer[d] and Developer[a] + Developer[b] != Developer[e] and Developer[c] + Developer[d] != Developer[e]: #모든 능력치가 서로 다른 경우
                        temp = [Developer[a] + Developer[b], Developer[c] + Developer[d], Developer[e]] #3개의 팀의 능력치 중
                        result.append(max(temp) - min(temp)) #최대의 값과 최소의 값의 차가 가장 낮은경우 result 배열에 대입

print(min(result))