while True:
    temp = input()
    if temp == "END":
        break
    else:
        tempList = list(temp)
        tempList.reverse()
        for i in tempList:
            print(i,end="")
    print()