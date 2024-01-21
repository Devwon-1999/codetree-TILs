class class_attitude():
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

n = int(input())
students = []
if n == 1:
    name, score = input().split()
    print(name)
else:
    for i in range(n):
        name, score = input().split()
        score = int(score)
        
        found = False
        for student in students:
            if student.name == name:
                student.score += score
                found = True
                break
        
        if not found:
            students.append(class_attitude(name, score))


    students_sorted = sorted(students, key=lambda x: x.score, reverse=True)
    lowest_score = students_sorted[-1].score
    second_lowest_score = None

    for student in reversed(students_sorted):
        if student.score > lowest_score:
            second_lowest_score = student.score
            break

    second_lowest_students = [student.name for student in students_sorted if student.score == second_lowest_score]

    if len(second_lowest_students) == 1:
        print(second_lowest_students[0])
    else:
        print("Tie")