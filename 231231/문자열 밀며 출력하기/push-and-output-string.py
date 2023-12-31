str = input()
result = str

while True:
    print(str)
    str = str[1:] + str[0]
    
    if result == str:
        print(str)
        break