a = list()

while True:
    age = int(input())
    if 20 <= age <= 29:
        a.append(age)
    
    if age <= 19 or age >= 30:
        avg = sum(a) / len(a)

        print("%.2f" % avg)
        break