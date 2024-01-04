n = int(input())

for i in range(n):
    temp = input()

    if temp.isalpha():
        print(temp)
    elif temp.isdigit():
        print(ord(temp))