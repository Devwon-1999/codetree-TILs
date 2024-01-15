def sum_a_to_b(a, b):
    result = 0
    for i in range(a - 1, b):
        result += A[i]

    return result


n, m = map(int, input().split())
A = list(map(int, input().split()))
result = 0
for i in range(m):
    a1, a2 = map(int, input().split())
    result = sum_a_to_b(a1, a2)

    print(result)