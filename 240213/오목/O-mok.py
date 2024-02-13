base = []

#가로 
widthx, widthy = [0, 1, 2, 3, 4], [0, 0, 0, 0, 0]
#세로
lengthx, lengthy = [0, 0, 0, 0, 0], [0, 1, 2, 3, 4]
#대각선
diagonalx, diagonaly = [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]

for i in range(19):
    temp = list(map(int, input().split()))
    base.append(temp)
result = []
for i in range(19 - 4):
    for j in range(19 - 4):
        if base[j][i] == 1:
            temp = []
            for x, y in zip(widthx, widthy):
                if base[j + y][i + x] == 1:
                    temp.append([j + y + 1, i + x + 1])
                else:
                    break

            for x, y in zip(lengthx, lengthy):
                if base[j + y][i + x] == 1:
                    temp.append([j + y + 1, i + x + 1])
                else:
                    break

            for x, y in zip(diagonalx, diagonaly):
                if base[j + y][i + x] == 1:
                    temp.append([j + y + 1, i + x + 1])
                else:
                    break

            if len(temp) == 5:
                result.append(temp)
        
        elif base[j][i] == 2:
            for x, y in zip(widthx, widthy):
                if base[j + y][i + x] == 1:
                    temp.append([j + y + 1], [i + x + 1])
                else:
                    break

            for x, y in zip(lengthx, lengthy):
                if base[j + y][i + x] == 1:
                    temp.append([j + y + 1, i + x + 1])
                else:
                    break

            for x, y in zip(diagonalx, diagonaly):
                if base[j + y][i + x] == 1:
                    temp.append([j + y + 1, i + x + 1])
                else:
                    break

            if len(temp) == 5:
                result.append(temp)
        if result:
            break
        else:
            continue


print(base[result[0][0][0]][result[0][0][1]])
print(result[0][2][0], result[0][2][1])