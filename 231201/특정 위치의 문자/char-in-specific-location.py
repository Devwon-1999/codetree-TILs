from sys import stdin
arr = ['L', 'E', 'B', 'R', 'O', 'S']
word = stdin.readline().strip()

key = True
for i, value in enumerate(arr):
    if value == word:
        print(i)
        key=False
        break
if key:
    print("None")