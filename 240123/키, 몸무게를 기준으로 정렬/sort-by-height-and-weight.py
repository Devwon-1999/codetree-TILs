class identity:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight
n = int(input())
base = []
for i in range(n):
    name, height, weight = input().split()
    height, weight = int(height), int(weight)
    base.append(identity(name, height, weight))

base.sort(key = lambda x :(x.height, -x.weight))

for i in range(len(base)):
    print(base[i].name, base[i].height, base[i].weight)