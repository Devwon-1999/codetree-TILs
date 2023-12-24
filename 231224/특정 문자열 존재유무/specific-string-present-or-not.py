n, search = input().split()
n = int(n)

for i in range(n):
    inputString = input()

    if search in inputString:
        print(inputString)