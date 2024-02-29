N = int(input())
LinkedList = []
for i in range(N):
    orderList = list(input().split())

    if orderList[0] == "push_front":
        LinkedList.insert(0, orderList[1])

    elif orderList[0] == "push_back":
        LinkedList.append(orderList[1])

    elif orderList[0] == "pop_front":
        target = LinkedList[0]
        LinkedList.pop(0)
        print(target)

    elif orderList[0] == "pop_back":
        target = LinkedList[-1]
        LinkedList.pop()
        print(target)

    elif orderList[0] == "size":
        print(len(LinkedList))

    elif orderList[0] == "empty":
        if LinkedList:
            print(0)
        else:
            print(1)

    elif orderList[0] == "front":
        print(LinkedList[0])

    elif orderList[0] == "back":
        print(LinkedList[-1])