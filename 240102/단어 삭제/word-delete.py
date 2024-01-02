s = input()
delete = input()

while True:
    if delete in s:
        s = s.replace(delete, "", 1)
    else:
        break

print(s)