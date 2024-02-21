x1, x2, x3, x4 = map(int, input().split())

answer = "nonintersecting"

for i in range(x1, x2 + 1):
    for j in range(x3, x4 + 1):
        if i == j:
            answer = "intersecting"
            
print(answer)