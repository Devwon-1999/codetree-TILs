sambae = 0
ohbae = 0
for _ in range(10):
    n = int(input())
    if n % 3 == 0:
        sambae += 1
    if n % 5 == 0:
        ohbae += 1

print(sambae,ohbae)