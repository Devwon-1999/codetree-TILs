s = input()

arr = list(s)
arr.pop(1)
arr.pop(-2)
s = ''.join(arr)
print(s)