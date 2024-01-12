def return_1_to_N(N):
    result = 0
    for i in range(1, N + 1):
        result += i

    return result // 10


N = int(input())

result = return_1_to_N(N)

print(result)