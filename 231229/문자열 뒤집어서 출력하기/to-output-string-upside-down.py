result = ""
results = []
for i in range(4):
    temp = list(input())
    temp.reverse()
    for i in temp:
        result += i
    results.append(result)
    result = ""

results.reverse()

for i in results:
    print(i)