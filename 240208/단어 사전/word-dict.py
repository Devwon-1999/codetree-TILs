sentence = list(input().split())
sentence.sort()
result = set()

for i in sentence:
    result.add(i)


for i in result:
    print(i, end = " ")