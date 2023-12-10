string = input()
n = int(input())

strLen = len(string)
cnt = 0

for i in range(strLen - 1, -1, -1):
	if cnt >= n:
		break
	print(string[i], end="")
	cnt += 1