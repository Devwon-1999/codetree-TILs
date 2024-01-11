base, num, trans = map(int, input().split())  
if base != 10:
    num = str(num)
    num_10 = int(num, base)

def solution(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        if mod >= 10:
            rev_base += chr(ord('A') + mod - 10)
        else:
            rev_base += str(mod)

    return rev_base[::-1]

print(solution(num_10, trans))