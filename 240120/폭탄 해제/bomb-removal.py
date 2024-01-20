class bomb_remove():
    def __init__ (self, code, color, sec):
        self.code = code
        self.color = color
        self.sec = sec

code, color, sec = input().split()
sec = int(sec)

bomb1 = bomb_remove(code, color, sec)


print(f"code : {bomb1.code}")
print(f"color : {bomb1.color}")
print(f"second : {bomb1.sec}")