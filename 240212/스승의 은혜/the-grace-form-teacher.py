N, B = map(int, input().split())

presents = []

for i in range(N):
    price, delivery = map(int, input().split())
    presents.append((price, delivery))

presents.sort(key=lambda x: (x[0] + x[1], x[0]))  # 가격 + 배송비가 적은 순서대로 정렬

max_students = 0
for i in range(N):
    total_cost = 0
    students = 0
    for j in range(N):
        if j == i:  # 쿠폰 사용 대상 학생
            if total_cost + presents[j][0] // 2 + presents[j][1] <= B:
                total_cost += presents[j][0] // 2 + presents[j][1]
                students += 1
        elif total_cost + presents[j][0] + presents[j][1] <= B:
            total_cost += presents[j][0] + presents[j][1]
            students += 1

    max_students = max(max_students, students)

print(max_students)