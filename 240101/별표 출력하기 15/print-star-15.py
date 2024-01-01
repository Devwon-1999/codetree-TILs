n = int(input())

string = "**"

for i in range(n, 0, -1):
    for j in range(i):
        print(string, end = "")
    print()
for i in range(2, n + 1):
    for j in range(i):
        print(string, end = "")
    print()