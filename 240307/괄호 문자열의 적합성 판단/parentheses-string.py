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

n = input()
s = Stack()
answer = []
for i in range(0, len(n)):
  if n[i] == "(":
    s.push("(")
  else:
    if s.empty() == 1:
      continue
    s.pop()
  if s.empty() == 0:
    answer.append(0)
  else:
    answer.append(1)

if 1 in answer:
  print("Yes")
else:
  print("No")