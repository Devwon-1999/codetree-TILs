inputStr = input()


strlist = list(inputStr)
strlist[1] = "a"
strlist[-2] = "a"
for i in strlist:
    print(i,end = "")