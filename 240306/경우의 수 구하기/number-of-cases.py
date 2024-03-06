n = int(input())

dic = dict()

for i in range(n):
    thing, group = input().split()
    if group in dic:
        if isinstance(dic[group], list):
            dic[group].append(thing)
        else:
            dic[group] = [dic[group], thing]
    else:
        dic[group] = thing

result = 1
for group in dic.values():
    if isinstance(group, list):
        result *= (len(group) + 1)
    else:
        result *= 2

print(result - 1)