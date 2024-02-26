def generate_combinations(lst):
    all_combinations = []
    n = len(lst)
    for i in range(1, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                combination = [[lst[m] for m in range(i)], [lst[m] for m in range(i, j)], [lst[m] for m in range(j, k)], [lst[m] for m in range(k, n)]]
                all_combinations.append(combination)
    return all_combinations

# 예시 리스트
my_list = [0, 1, 2, 3, 4]

# 모든 경우의 수 생성
combinations = generate_combinations(my_list)
print(combinations)