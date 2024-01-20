class address:
    def __init__(self, name, address, place):
        self.name = name
        self.address = address
        self.place = place

n = int(input())

nameList = []
people = []
for i in range(n):
    na, ad, pl = input().split()

    nameList.append(na)

    nameList.sort()

    people.append(address(na, ad, pl))

for i in range(n):
    if people[i].name == nameList[-1]:
        print(f"name {people[i].name}")
        print(f"addr {people[i].address}")
        print(f"city {people[i].place}")





# agents_score = []
# for i in range(5):
#     agents_score.append(agents[i].score)

# min_S = min(agents_score)
# min_N = ""
# for i in range(5):
#     if agents[i].score == min_S:
#         min_N = agents[i].name


# print(min_N, min_S)