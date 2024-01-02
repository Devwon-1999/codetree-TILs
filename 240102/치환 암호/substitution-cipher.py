key = input()
original = "abcdefghijklmnopqrstuvwxyz"
rule = input()

for i in key:
    cnt = 0
    if i == " ":
        print(" ", end = "")
        continue
    for j in rule:
        cnt += 1
        if i == j:
            print(original[cnt-1], end = "")