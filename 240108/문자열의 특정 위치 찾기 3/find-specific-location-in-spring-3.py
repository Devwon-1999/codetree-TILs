baseStr = input()
search = input()

if baseStr.find(search):
    print(baseStr.find(search) + 1)
if baseStr.find(search) == -1:
    print('Not Found')