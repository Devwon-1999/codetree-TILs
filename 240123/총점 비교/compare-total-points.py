class score:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

n = int(input())
base = []
for i in range(n):
    name, kor, eng, math = input().split()
    kor, eng, math = int(kor), int(eng), int(math)
    base.append(score(name, kor, eng, math))

base.sort(key = lambda x: x.kor + x.eng + x.math)

for i in range(len(base)):
    print(base[i].name, base[i].kor, base[i].eng, base[i].math)