class score:
    def __init__(self, name, kor, english, math):
        self.name = name
        self.kor = kor
        self.english = english
        self.math = math

    
n = int(input())
base = []
for i in range(n):
    name, kor, english, math = input().split()
    kor, english, math = int(kor), int(english), int(math)
    base.append(score(name, kor, english, math))

base.sort(key = lambda x: (-x.kor, -x.english, -x.math))

for i in range(len(base)):
    print(base[i].name, base[i].kor, base[i].english, base[i].math)