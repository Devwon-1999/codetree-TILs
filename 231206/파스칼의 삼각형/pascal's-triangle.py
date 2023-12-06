n = int(input()) 
numList = list()
tempList = list() 

for i in range(n): 
    numList.append(1) 
    tempList.append(1) 
    if i < 2: 
        pass 
    else:
        for j in range(1, len(numList)-1): 
            tempList[j] = numList[j-1]+numList[j]
    for j in range(len(numList)): 
        numList[j]=tempList[j]
        print(str(numList[j]) + " ", end="") 
    print("")