class identity:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

base = []
for i in range(5):
    name, height, weight = input().split()
    height, weight = int(height), float(weight)
    base.append(identity(name, height, weight))

base.sort(key = lambda x :(x.name))

print("name")
for i in range(len(base)):
    print(base[i].name, base[i].height, "%.1f" % base[i].weight)

print()

base.sort(key = lambda x :(-x.height))

print("height")
for i in range(len(base)):
    print(base[i].name, base[i].height, "%.1f" % base[i].weight)