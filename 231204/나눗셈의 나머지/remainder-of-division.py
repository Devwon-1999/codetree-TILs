a, b = map(int,input().split())

remainderDic = {i: 0 for i in range(b)}

while a > 1:
    remainder = a % b
    remainderDic[remainder] += 1
    a //= b

result = sum(count**2 for count in remainderDic.values())
print(result)