N = input()
N_list = []
for i in N:
    N_list.append(i)

N_10 = 0
for i in N_list:
    i = int(i)
    N_10 = N_10 * 2 + i

N_10 *= 17

result = []
while N_10 > 0:
    digit = N_10 % 2
    N_10 = N_10 // 2
    result.append(digit)

for i in range(len(result) - 1, -1, -1):
    print(result[i], end = "")