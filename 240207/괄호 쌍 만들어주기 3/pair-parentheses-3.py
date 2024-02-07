string = input()
string_List = []
for i in string:
    string_List.append(i)

cnt = 0
for i in range(len(string)):
    for j in range(len(string)):
        if string_List[i] == "(":
            if i < j and string_List[j] == ")":
                cnt += 1
                
print(cnt)