n = int(input())

Queue = []

def push(A):
    global Queue
    Queue.append(A)

def pop():
    global Queue
    if Queue:
        print(Queue[0])
        Queue = Queue[1:]
    else:
        print(-1)

def size():
    global Queue
    print(len(Queue))

def empty():
    global Queue
    if Queue:
        print(0)
    else:
        print(1)
    
def front():
    global Queue
    if Queue:
        print(Queue[0])
    else:
        print(-1)

def back():
    global Queue
    if Queue:
        print(Queue[-1])
    else:
        print(-1)

for i in range(n):
    order = input()
    if " " in order:
        order, num = order.split()
        if order == "push":
            push(num)
            print(num)
    else:
        if order == "pop":
            pop()
        elif order == "size":
            size()
        elif order == "empty":
            empty()
        elif order == "front":
            front()
        elif order == "back":
            back()