n = int(input())
result = list()

for i in range(n):
    arr = list(map(int, input().split()))
    if sum(arr) / len(arr) >= 60:
        result.append("pass")
    else:
        result.append("fail")

for i in result:
    print(i)
print(result.count("pass"))