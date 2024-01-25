n = int(input())

cur = 0
segments = []

for _ in range(n):
    distance, direction = tuple(input().split())
    distance = int(distance)

    section_left, section_right = 0, 0

    if direction == 'L':
        section_left = cur - distance
        section_right = cur
        cur -= distance
    else:
        section_left = cur
        section_right = cur + distance
        cur += distance

    segments.append([section_left, section_right])


visited_count = [0] * 2001  

for segment in segments:
    for i in range(segment[0], segment[1]):
        visited_count[i] += 1

answer = sum(1 for count in visited_count if count >= 2)
print(answer)