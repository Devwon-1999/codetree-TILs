class student:
    def __init__(self, height, weight, num):
        self.height = height
        self.weight = weight
        self.num = num

N = int(input())

students = []

for i in range(N):
    height, weight = map(int, input().split())
    students.append(student(height, weight, i + 1))

students.sort(key = lambda x : (x.height, -x.weight))

for i in range(len(students)):
    print(students[i].height, students[i].weight, students[i].num)