def part_of_sequence(list1, list2):
    if all(x in list1 for x in list2):
        return True
    else:
        return False


n1, n2 = map(int, input().split())
numList1 = list(map(int, input().split()))
numList2 = list(map(int, input().split()))

if part_of_sequence(numList1,numList2):
    print("Yes")
else:
    print("No")