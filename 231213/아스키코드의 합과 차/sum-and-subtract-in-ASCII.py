a, b = input().split()

acia = ord(a)
acib = ord(b)

add = acia + acib
sub = 0
if acia > acib:
    sub = acia - acib
else:
    sub = acib - acia
    
print(add, sub)