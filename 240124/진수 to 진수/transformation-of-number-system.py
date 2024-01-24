a, b = input().split() # a 진수 -> b 진수
n = input() # a 진수 n

# a진수 n을 10진수로
list_a = []
for i in n: # n을 리스트로 한개씩 분리
    list_a.append(i)

a = int(a)
num = 0 # 10진수 저장할 변수

for i in list_a:
    i = int(i)
    num = num * a + i

# 10진수를 n을 b 진수로
result = []
while num > 0:
    digit = num % 2
    num = num // 2
    result.append(digit)

for i in range(len(result) - 1, -1, -1):
    print(result[i], end = "")