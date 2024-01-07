n = int(input())

scoreList = list(map(float, input().split()))

print("%.1f" % (sum(scoreList) / n))