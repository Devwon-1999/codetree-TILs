baseStr = input()
search = input()


if baseStr.find(search) == -1:
    print('Not Found')

elif baseStr.find(search):
    print(baseStr.find(search) + 1)