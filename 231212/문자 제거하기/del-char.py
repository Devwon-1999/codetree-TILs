s = input()
arr = list(s)
while len(s) > 0:
    n = int(input())
    if n > len(s):
        arr.pop(-1)
        s = ''.join(arr)
        print(s)
        break     
    else:
        arr.pop(n)
        s = ''.join(arr)
    print(s)