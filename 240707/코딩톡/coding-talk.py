n, m, p = map(int,input().split())
#n사람수, m 메시지 수, p 메시지 번호

developer = []

a = 65
for i in range(n):
    developer.append(chr(a))
    a += 1

message = []
for i in range(m):
    #c 메시지 u 안읽은 사람의 수
    c,  u = input().split()
    u = int(i)
    message.append([c, u])

for i in range(p - 1, n):
    if message[i][0] in developer:
        developer.remove(message[i][0])

for i in developer:
    print(i, end = " ")