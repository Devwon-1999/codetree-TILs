N = int(input())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

list1.sort()
list2.sort()

if len(list1) == len(list2):
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            print("No")
            break
    print("Yes")
else:
    print("No")