n = int(input())

alphaList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

firstIndex = (n*n) % 26 - 1
setupIndex = firstIndex
for i in range(1, n+1):
    for j in range(1, n+1):
        print(alphaList[firstIndex], end = " ")
        firstIndex -= n
    print()
    firstIndex = setupIndex - i