def print_min_common_multiple(n, m):
    result = 0

    n_mul = []
    m_mul = []

    for i in range(1, m + 1):
        n_mul.append(n * i)

    for i in range(1, n + 1):
        m_mul.append(m * i)

    for i in n_mul:
        for j in m_mul:
            if i == j:
                print(i)
                break
        if i == j:
            break


n, m = map(int, input().split())

print_min_common_multiple(n, m)