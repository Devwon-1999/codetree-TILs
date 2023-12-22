n = int(input())

for i in range(n):
    temp = int(input())
    if temp < 0:
        print("minus")
    elif temp > 0:
        print("plus")
    else:
        print("zero")