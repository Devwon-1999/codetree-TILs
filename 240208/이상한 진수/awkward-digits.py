def find_N(a, b):
    for i in range(len(a)):
        for j in range(len(b)):
            for replacement_a in range(2): 
                for replacement_b in range(3):

                    a_result = int(a[:i] + str(replacement_a) + a[i+1:], 2)
                    

                    b_result = int(b[:j] + str(replacement_b) + b[j+1:], 3)
                    

                    if a_result == b_result:
                        return a_result


a = input().strip()
b = input().strip()


result = find_N(a, b)
if result is not None:
    print(result)