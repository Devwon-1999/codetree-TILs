class address:
    def __init__(self, name, address, place):
        self.name = name
        self.address = address
        self.place = place

n = int(input())

nameList = []
for i in range(n):
    na, ad, pl = input().split()

    nameList.append(na)

    nameList.sort()

    na = address(na, ad, pl)


if na.name == nameList[-1]:
    print(f"name {na.name}")
    print(f"addr {na.address}")
    print(f"city {na.place}")