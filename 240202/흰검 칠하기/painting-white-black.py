n = int(input())
now = 5000
result = [" " for i in range(10001)]
blackcnt = [0 for i in range(10001)]
whitecnt = [0 for i in range(10001)]

for i in range(n):
	length, order = input().split()

	length = int(length)


	if order == "L": #흰색
		for i in range(now, now - length, -1):
			result[i] = "white"
			whitecnt[i] += 1

		now -= length -1
	
	elif order == "R": #검은색
		for i in range(now, now + length):
			result[i] = "black"
			blackcnt[i] += 1
		
		now += length -1

for i in range(len(blackcnt)):
	if blackcnt[i] < 2 or whitecnt[i] < 2:
		continue
	elif blackcnt[i] >= 2 and whitecnt[i] >= 2:
		result[i] = "grey"

result_white = 0
result_black = 0
result_grey = 0
for i in result:
	if i == " ":
		continue
	elif i == "black":
		result_black += 1
	elif i == "grey":
		result_grey += 1
	elif i == "white":
		result_white += 1

print(result_white, result_black, result_grey)