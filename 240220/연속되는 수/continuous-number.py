N = int(input()) # 입력될 수의 개수

base = [] # 입력된 수
for i in range(N):
    temp = int(input())
    base.append(temp)

delete = [] #지워질 수
for i in base:
    if i in delete:
        continue
    else:
        delete.append(i)

print(base)
print(delete)

caseList = [] # 테스트할 리스트들:
for i in range(len(delete)):
    if delete[i] in base:
        pass
unique_list = []
[unique_list.append(x) for x in my_list if x not in unique_list]
print(unique_list)