class weather:
    def __init__(self, date, day, weather):
        self.day = day
        self.date = date
        self.weather = weather

n = int(input())
dateList = []
weathers = []
for i in range(n):
    date, day, weather1 = input().split()
    if weather1 == "Rain":
        dateList.append(date)
    dateList.sort()

    weathers.append(weather(date, day, weather1))


for i in range(n):
    if dateList[0] == weathers[i].date:
        print(weathers[i].date, weathers[i].day, weathers[i].weather)