class product:
    def __init__(self, name, code):
        self.name = name
        self.code = code

pd1 = product("codetree", "50")
name, code = input().split()

pd2 = product(name, code)

print(f"product {pd1.code} is {pd1.name}")
print(f"product {pd2.code} is {pd2.name}")