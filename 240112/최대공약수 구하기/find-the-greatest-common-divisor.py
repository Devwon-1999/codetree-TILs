def max_measure(n, m):
    n_measure = []
    m_measure = []
    max_measure = 0

    for i in range(1, n + 1):
        if n % i == 0:
            n_measure.append(i)
    for i in range(1, m + 1):
        if m % i == 0:
            m_measure.append(i)

    for i in n_measure:
        for j in m_measure:
            if i == j:
                max_measure = i
    
    print(max_measure)


n, m = map(int, input().split())

max_measure(n, m)