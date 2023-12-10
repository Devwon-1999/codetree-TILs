s = str(input())
n = int(input())

if n > len(s) :
    print(reverse(s))
else :     
    print(s[-1:len(s) - n - 1:-1])