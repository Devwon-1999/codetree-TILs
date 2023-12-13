A = input()
arr = list(A)
if "e" in A:
    eindex = A.find("e")
    arr.pop(eindex)
    A = ''.join(arr)
    print(A)