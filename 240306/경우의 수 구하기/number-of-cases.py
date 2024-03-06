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

print(dic)
print(type(dic))