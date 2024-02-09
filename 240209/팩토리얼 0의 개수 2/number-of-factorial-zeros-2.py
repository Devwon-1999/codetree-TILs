n = int(input())

Factorial = 1
for i in range(1, n + 1):
    Factorial *= i

str_Factorial = str(Factorial)

list_Factorial = []

for i in str_Factorial:
    list_Factorial.append(i)

list_Factorial.reverse()

cnt = 0

for i in list_Factorial:
    if i == "0":
        cnt += 1
    else:
        break

print(cnt)