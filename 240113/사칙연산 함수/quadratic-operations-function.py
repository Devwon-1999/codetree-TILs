def plus(a, b):
    print(f"{a} + {b} = {a + b}")
def minus(a, b):
    print(f"{a} - {b} = {a - b}")   
def mul(a, b):
    print(f"{a} * {b} = {a * b}")   
def div(a, b):
    print(f"{a} / {b} = {a // b}")   


def order_check(a, b, o):
    if o == "+":
        plus(a, b)
    elif o == "-":
        minus(a, b)
    elif o == "*":
        mul(a, b)
    elif o == "/":
        div(a, b)
    else:
        print("False")


a, order, c = input().split()

a, c = int(a), int(c)

order_check(a, c, order)