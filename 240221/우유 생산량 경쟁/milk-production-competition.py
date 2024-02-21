N = int(input())

recode = []
for i in range(N):
    date, cow_name, milk = input().split()
    date, milk = int(date), int(milk)

    recode.append([date, cow_name, milk])

sorted_recode = sorted(recode, key=lambda x: x[0])

Ranking = {"Bessie": 7, "Elsie": 7, "Mildred": 7}
previous_top_cows = set(["Bessie", "Elsie", "Mildred"])
name_changes = 0

for date, cow_name, milk in sorted_recode:
    Ranking[cow_name] += milk
    top_cows = [cow for cow, milk in Ranking.items() if milk == max(Ranking.values())]

    if set(top_cows) != previous_top_cows:
        name_changes += 1
        previous_top_cows = set(top_cows)

print(name_changes)