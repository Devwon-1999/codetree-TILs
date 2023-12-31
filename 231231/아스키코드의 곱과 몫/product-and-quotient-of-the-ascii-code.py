a, b = input().split()
mul = ord(a) * ord(b)

if ord(a) > ord(b):
    sub = ord(a) - ord(b)
else:
    sub = ord(b) - ord(a)
    
print(mul, sub)