n = int(input())

current_char = ord('A')
square = [[' ' for _ in range(n)] for _ in range(n)]

for col in range(n - 1, -1, -1):
    for row in range(n - 1, -1, -1):
        square[row][col] = chr(current_char)
        current_char = (current_char - ord('A') + 1) % 26 + ord('A')

for row in range(n):
    print(' '.join(square[row]))