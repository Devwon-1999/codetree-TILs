def printStr(n):
    if n > 0:
        print("Coding is my favorite hobby!")
    else:
        return 0
    printStr(n-1)

n = int(input())

printStr(n)