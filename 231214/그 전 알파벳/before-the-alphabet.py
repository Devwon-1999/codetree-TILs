a = input()

inta = ord(a)

resulta = inta - 1

if resulta <= 97:
    resulta = 122
    
print(chr(resulta))