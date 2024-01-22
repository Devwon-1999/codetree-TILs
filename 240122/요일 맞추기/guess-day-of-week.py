month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
date = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

m1, d1, m2, d2 = tuple(map(int, input().split()))

def month_date(m):
    m_date = 0
    for i in range(1, m):
        m_date += month[i]
    return m_date

m_date = month_date(m2) - month_date(m1)
total_date = m_date + (d2 - d1)

if total_date < 0:
    total_date += 7

print(date[total_date % 7])