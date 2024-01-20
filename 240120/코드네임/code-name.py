class codename:
    def __init__(self, name = " ", score = 0):
        self.name = name
        self.score = score


agents = []  
for i in range(5):
    name, score = input().split()
    score = int(score)
    agents.append(codename(name, score))


agents_score = []
for i in range(5):
    agents_score.append(agents[i].score)

min_S = min(agents_score)
min_N = ""
for i in range(5):
    if agents[i].score == min_S:
        min_N = agents[i].name


print(min_N, min_S)