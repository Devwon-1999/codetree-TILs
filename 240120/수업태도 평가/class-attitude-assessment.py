class class_attitude():
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score


n = int(input())

students = []

for i in range(n):
    name, score = input().split()
    score = int(score)
    for j in range(len(students)):
        if students[j].name == name:
            students[j].score += score
        else:
            students.append(class_attitude(name, score))

for i in range(len(students)):
    print(students[i].name, students[i].score)