a = input()
b = input()

sorted_a_list = sorted(a)
sorted_b_list = sorted(b)

sorted_a_str = "".join(sorted_a_list)
sorted_b_str = "".join(sorted_b_list)

if sorted_a_str == sorted_b_str:
    print("Yes")
else:
    print("No")