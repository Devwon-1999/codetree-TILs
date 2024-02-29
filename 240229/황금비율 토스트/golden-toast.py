n, m = map(int, input().split())

password = list(input())
index = n
for i in range(m):
    input_val = list(input().split())

    if input_val[0] == "L":
        if index == 0:
            continue
        else:
            index -= 1
    elif input_val[0] == "R":
        if index == n - 1:
            continue
        else:
            index += 1

    elif input_val[0] == "D":
        if index == n:
            continue
        else:
            password.pop(index + 1)
    
    elif input_val[0] == "P":
        password.insert(index, input_val[1])

for i in password:
    print(i, end = "")