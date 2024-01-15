def is_part_of(a, b):
    a = str(a)
    b = str(b)

    if b in a:
        return True
    else:
        return False


def find_first_index(a, b):
    first_index = a.index(b)
    return first_index


base = input()
search = input()
index = -1
if is_part_of(base, search):
    index = find_first_index(base, search)
    print(index)
else:
    print(index)