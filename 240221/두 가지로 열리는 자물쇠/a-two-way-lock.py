from itertools import product

def is_valid_combination(combination, lock, N):
    for i in range(3):
        if abs(combination[i] - lock[i]) > 2 and abs(combination[i] - lock[i]) < N - 2:
            return False
    return True

def count_valid_combinations(N, first_combination, second_combination):
    valid_combinations = set()
    for combination in product(range(1, N + 1), repeat=3):
        if is_valid_combination(combination, first_combination, N) or is_valid_combination(combination, second_combination, N):
            valid_combinations.add(combination)
    return len(valid_combinations)

# 입력
N = int(input())
first_combination = tuple(map(int, input().split()))
second_combination = tuple(map(int, input().split()))

# 출력
print(count_valid_combinations(N, first_combination, second_combination))