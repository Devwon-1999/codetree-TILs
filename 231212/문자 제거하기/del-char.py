s = input()
arr = list(s)
while len(s) > 1:
    n = int(input())
    if n >= len(s):
        arr.pop(-1)
        s = ''.join(arr)   
    else:
        arr.pop(n)
        s = ''.join(arr)
    print(s)