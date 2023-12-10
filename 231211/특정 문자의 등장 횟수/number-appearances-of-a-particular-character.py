s = input()
eecnt = 0
ebcnt = 0

for i in range(len(s) - 1):
    if s[i] == 'e' and s[i + 1] == 'e':
        eecnt += 1   

for i in range(len(s) - 1):
    if s[i] == 'e' and s[i + 1] == 'b':
        ebcnt += 1

    

print(eecnt, ebcnt)