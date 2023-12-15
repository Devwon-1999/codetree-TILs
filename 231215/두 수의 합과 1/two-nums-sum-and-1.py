a, b = map(int, input().split())
cnt = 0
add = a + b

add = str(add)

for i in add:
    if i == "1":
        cnt += 1
print(cnt)