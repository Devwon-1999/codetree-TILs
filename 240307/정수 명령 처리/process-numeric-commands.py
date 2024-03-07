class Stack:
    def __init__(self):          
        self.items = []
                
    def push(self, item):        
        self.items.append(item)
                
    def empty(self):             
        if len(self.items) == 0:
            return 1
        else:
            return 0
                
    def size(self):              
        return len(self.items)
        
    def pop(self):               
        if self.empty():
            raise Exception("Stack is empty")
            
        return self.items.pop()
                
    def top(self):               
        if self.empty():
            raise Exception("Stack is empty")
                        
        return self.items[-1]


N = int(input())
s = Stack()
for i in range(N):
    temp = list(input().split())

    if temp[0] == "push":
        s.push(temp[1])
    elif temp[0] == "pop":
        print(s.pop())
    elif temp[0] == "size":
        print(s.size())
    elif temp[0] == "empty":  
        print(s.empty())
    elif temp[0] == "top":
        print(s.top())