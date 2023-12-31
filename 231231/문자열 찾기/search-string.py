s = input()
koicnt = 0
ioicnt = 0
for i in range(len(s)-2):
    if s[i] + s[i+1] + s[i+2] == "KOI":
        koicnt += 1
    elif s[i] + s[i+1] + s[i+2] == "IOI":
        ioicnt += 1

print(koicnt, ioicnt)