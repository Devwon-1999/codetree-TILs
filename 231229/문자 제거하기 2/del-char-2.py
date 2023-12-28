string, order = input().split()

order = int(order)

for i in range(order):
    temp = int(input())

    if temp > len(string):
        continue
    else:
        string = string[:temp-1] + string[temp:]
    print(string)