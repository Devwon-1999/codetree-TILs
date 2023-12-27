n = int(input())
total = []
score = []
A = []
B = []
C = []
D = []
for i in range(4):
    temp = list(input().split())

    if temp[0] == "A:":
        for i in temp:
            if i.isdigit():
                i = int(i)
                A.append(i)
        total.append(A)

    elif temp[0] == "B:":
        for i in temp:
            if i.isdigit():
                i = int(i)
                B.append(i)
        total.append(B)

    elif temp[0] == "C:":
        for i in temp:
            if i.isdigit():
                i = int(i)
                C.append(i)
        total.append(C)

    elif temp[0] == "D:":
        for i in temp:
            if i.isdigit():
                i = int(i)
                D.append(i)
        total.append(D)

print(f"A - {sum(A)}")
print(f"B - {sum(B)}")
print(f"C - {sum(C)}")
print(f"D - {sum(D)}")

for i in total:
    score.append(sum(i))

if max(score) == sum(A):
    print("Class A is winner!")
elif max(score) == sum(B):
    print("Class B is winner!")
elif max(score) == sum(C):
    print("Class C is winner!")
elif max(score) == sum(D):
    print("Class D is winner!")