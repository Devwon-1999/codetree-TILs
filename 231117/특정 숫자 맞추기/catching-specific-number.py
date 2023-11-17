num = 25
while True:
    n = int(input())
    if n > num:
        print("Lower")
    elif n < num:
        print("Higher")
    elif n == num:
        print("Good")