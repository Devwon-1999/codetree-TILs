s = input()

arr = list(s)
arr.pop(2)
arr.pop(-2)
s = ''.join(arr)
print(s)