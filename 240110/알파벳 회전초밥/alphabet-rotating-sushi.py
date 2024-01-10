A = input()
B = input()

repeat_count = 1
current_position = 0

while B:
    current_char = B[0]

    while A[current_position] != current_char:
        current_position += 1
        if current_position == len(A):
            current_position = 0
            repeat_count += 1

    B = B[1:]

    current_position += 1
    if current_position == len(A):
        current_position = 0

print(repeat_count)