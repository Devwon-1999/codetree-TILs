sex = int(input())
age = int(input())

if sex == 0 and age >= 19:
    print("M")
elif sex == 0 and age < 19:
    print("B")

elif sex == 1 and age >= 19:
    print("W")
elif sex == 1 and age < 19:
    print("G")