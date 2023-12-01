a,b=map(int,input().split())
arr=[a%b] 
f=[]
h=0
for _ in range(1000):
    if a//b<= 1:
        break
    a=a//b
    c=a%b
    arr.append(c)
    
    
for i in range(9):
    cnt=0
    s=0
    for j in arr:
        if j==i:
            cnt+=1
            s=cnt**2
    f.append(s)

for k in f:
    h+=k
print(h)