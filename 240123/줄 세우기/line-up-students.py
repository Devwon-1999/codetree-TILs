class student:
    def __init__(self, height, weight, num):
        self.height = height
        self.weight = weight
        self.num = num

N = int(input())
base = []
for i in range(N):
    height, weight = map(int, input().split())
    height, weight = int(height), int(weight)
    base.append(student(height, weight, i+1))

base.sort(key = lambda x :(-x.height, -x.weight, x.num))

for i in range(len(base)):
    print(base[i].height, base[i].weight, base[i].num)