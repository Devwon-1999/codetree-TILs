amath, aeng = map(int, input().split())
bmath, beng = map(int, input().split())
if amath > bmath:
    print("A")
else:
    print("B")

if (amath == bmath) and aeng > beng:
    print("A")
elif (amath == bmath) and aeng < beng:
    print("B")