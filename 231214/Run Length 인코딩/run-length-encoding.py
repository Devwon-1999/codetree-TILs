input_str = input()

result = []  
count = 1


for i in range(1, len(input_str)):
    if input_str[i] == input_str[i - 1]:
        count += 1
    else:
        result.append(input_str[i - 1] + str(count))
        count = 1


result.append(input_str[-1] + str(count))


print(len("".join(result)))
print("".join(result))