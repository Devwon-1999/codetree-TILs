def add(a, b): # +
    print(f"{a} + {b} = {a + b}")

def sub(a, b): # -
    print(f"{a} - {b} = {a - b}")

def mul(a, b): # *
    print(f"{a} * {b} = {a * b}")

def div(a, b): # /
    print(f"{a} / {b} = {a // b}")

num1, order, num2 = input().split()

num1, num2 = int(num1), int(num2)

if order == "+":
    add(num1, num2)
elif order == "-":
    sub(num1, num2)
elif order == "*":
    mul(num1, num2)
elif order == "/":
    div(num1, num2)