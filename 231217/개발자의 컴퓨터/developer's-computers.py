dic = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0,
 "9": 0, "10": 0, "11": 0, "12": 0, "13": 0, "14": 0, "15": 0, "16": 0, 
 "17": 0, "18": 0, "19": 0, "20": 0, "21": 0, "22": 0, "23": 0, "24": 0
}

N = int(input())
maxValue = 0
for i in range(N):
    start, end, computer = map(int, input().split())

    for i in range(start, end+1):
        i = str(i)
        dic[i] += computer

for key, value in dic.items():
    if maxValue < value:
        maxValue = value

print(maxValue)