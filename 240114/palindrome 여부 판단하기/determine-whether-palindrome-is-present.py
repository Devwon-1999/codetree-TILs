def palindrome(string):
    reverse_string = "".join(reversed(string))
    if string == reverse_string:
        return True
    else:
        return False


A = input()
if palindrome(A):
    print("Yes")
else:
    print("No")