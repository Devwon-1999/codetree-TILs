class identity():
    def __init__(self, _id, _level):
        self._id = _id
        self._level = _level

_id, _level = input().split()

user1 = identity("codetree", 10)
user2 = identity(_id, _level)

print("user", user1._id, "lv", user1._level)
print("user", user2._id, "lv", user2._level)