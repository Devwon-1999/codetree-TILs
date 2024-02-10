N = int(input())
string = input()

result = []

for i in range(N):
    for j in range(i, N):
        for k in range(i, N):
            if string[i] == "C" and string[j] == "O" and string[k] == "W":
                result.append([i+1, j+1, k+1])

print(len(result))