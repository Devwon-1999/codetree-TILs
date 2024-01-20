def calculate_distance(A, B):
    current_position = A
    total_distance = 0
    step = 1

    while current_position != B:
        total_distance += abs(step)
        current_position += step
        step *= -2

    
    return total_distance 


A, B = map(int, input().split())


result = calculate_distance(A, B)
print(result)