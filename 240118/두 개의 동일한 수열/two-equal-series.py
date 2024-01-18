N = int(input())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

list1.sort()
list2.sort()

is_same = True

for i in range(len(list1)):
    if list1[i] != list2[i]:
        print("No")
        is_same = False
        break

if is_same:
    print("Yes")