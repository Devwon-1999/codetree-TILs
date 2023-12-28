cnt = 1
result = []
while True:
    temp = input()
    if temp == "0":
        break

    if cnt % 2 == 0:
        result.append(temp)
    cnt += 1    

print(cnt-1)
for i in result:
    print(i)