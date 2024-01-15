def alpha_check(a):
    result = []

    for i in a:
        if i not in result:
            result.append(i)

    if len(result) >= 2:
        return True
    else:
        return False


A = input()

if alpha_check(A):
    print("Yes")
else:
    print("No")