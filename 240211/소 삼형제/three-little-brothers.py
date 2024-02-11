N = int(input())
visits = {}


for _ in range(N):
    group = input().split()
    key = tuple(sorted(group))  
    visits[key] = visits.get(key, 0) + 1


max_visits = max(visits.values())

print(max_visits)