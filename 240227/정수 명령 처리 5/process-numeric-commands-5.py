N = int(input())
arr = []
for i in range(N):
    temp = list(input().split())
    if temp[0] == "push_back":
        arr.append(temp[1])
    elif temp[0] == "pop_back":
        arr.pop()
    elif temp[0] == "size":
        print(len(arr))
    elif temp[0] == "get":
        print(arr[int(temp[1]) - 1])