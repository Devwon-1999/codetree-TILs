n = int(input())
inputStr = ""
cnt = 0
for i in range(n):
    temp = input()
    inputStr += temp

for i in inputStr:
    cnt += 1
    print(i,end="")
    if cnt == (len(inputStr) // 2):
        print()