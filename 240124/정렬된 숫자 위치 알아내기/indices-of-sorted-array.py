N = int(input())
numList = list(map(int, input().split()))


sorted_indices = sorted(range(N), key=lambda i: numList[i])


before_sort = [0] * N
for i, idx in enumerate(sorted_indices):
    before_sort[idx] = i + 1


for i in before_sort:
    print(i, end=" ")