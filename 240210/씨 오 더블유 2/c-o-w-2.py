N = int(input())
string = input()

result = []

for i in range(N):
    if string[i] == "C":
        for j in range(i, N):
            if string[j] == "O":
                for k in range(i, N):
                    if string[k] == "W":
                        result.append([i+1, j+1, k+1])

print(len(result))