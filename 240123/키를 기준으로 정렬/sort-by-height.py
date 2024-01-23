class student:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    
n = int(input())
base = []
for i in range(n):
    name, height, weight = input().split()
    base.append(student(name, height, weight))

base.sort(key = lambda x: x.height)

for i in range(len(base)):
    print(base[i].name, base[i].height, base[i].weight)