def calculate_distance(start, end):
    current = start
    distance = 0
    step = 1

    while current != end:
        if current < end:
            current += step
        else:
            current -= step

        distance += step
        step *= 2  

    return distance


A, B = map(int, input().split())


result = calculate_distance(A, B)
print(result)