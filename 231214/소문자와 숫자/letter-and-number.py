s = input()

for i in s:
    if i.isalpha() or i.isdigit():
        print(i.lower(), end="")