n = int(input())
now = 5000
result = [" " for i in range(10001)]

for i in range(n):
	size, order = input().split()
	size = int(size)	

	if order == "L": #왼쪽으로
		for i in range(now, now - size, -1):
			if result[i] == " " or result[i] == "black":
				result[i] = "white"
		now -= size - 1

	elif order == "R": #오른쪽으로
		for i in range(now, now + size):
			if result[i] == " " or result[i] == "white":
				result[i] = "black"
		now += size - 1


black_cnt = 0
white_cnt = 0
for i in result:
	if i == " ":
		continue
	elif i == "black":
		black_cnt += 1
	elif i == "white":
		white_cnt += 1


print(white_cnt, black_cnt)