n = int(input())
holcnt = 0
jjakcnt = 0
for i in range(n):
    num = int(input())
    if num == 0:
        break
    if num % 2 == 1:
        holcnt += 1
    else:
        jjakcnt += 1

print(jjakcnt)
print(holcnt)