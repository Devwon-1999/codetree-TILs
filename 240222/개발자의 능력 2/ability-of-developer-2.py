from itertools import combinations

numbers = [0, 1, 2, 3, 4, 5]
base = []

# 주어진 숫자들에서 가능한 모든 3묶음 조합 생성
for combo in combinations(numbers, 2):
    remaining = [num for num in numbers if num not in combo]
    for remaining_combo in combinations(remaining, 2):
        remaining_2 = [num for num in remaining if num not in remaining_combo]
        base.append([list(combo), list(remaining_combo), list(remaining_2)])


numList = list(map(int, input().split()))
answer = []
min_val = 9999999

for combination in base:
    temp = []
    for x, y in combination:
        temp.append(numList[x] + numList[y])
    min_val = min(min_val, max(temp) - min(temp))

print(min_val)