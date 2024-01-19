class _007:
    def __init__(self, code, place, time):
        self.code = code
        self.place = place
        self.time = time

    def print_all(self):
        print(f"secret code : {code}")
        print(f"meeting point : {place}")
        print(f"time : {time}")

code, place, time = input().split()

print_007 = _007(code,place,time)

print_007.print_all()