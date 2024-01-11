formation, fNum, t_formation = map(int, input().split())
fNum = str(fNum)
if formation != 10:
    fNum = int(fNum, formation)

if t_formation < 10:
    result_1 = fNum % t_formation
    result_10 = fNum // t_formation
    print(result_10, result_1, sep = "")
elif t_formation >= 10:
    result_1 = fNum % t_formation
    if result_1 == 10:
        result_1 = "a"
    elif result_1 == 11:
        result_1 = "b"
    elif result_1 == 12:
        result_1 = "c"
    elif result_1 == 13:
        result_1 = "d"
    elif result_1 == 14:
        result_1 = "e"
    elif result_1 == 15:
        result_1 = "f"
    elif result_1 == 16:
        result_1 = "g"
    elif result_1 == 17:
        result_1 = "h"
    elif result_1 == 18:
        result_1 = "i"
    elif result_1 == 19:
        result_1 = "j"
    elif result_1 == 20:
        result_1 = "k"
    elif result_1 == 21:
        result_1 = "l"
    elif result_1 == 22:
        result_1 = "m"
    elif result_1 == 23:
        result_1 = "n"
    elif result_1 == 24:
        result_1 = "o"
    elif result_1 == 25:
        result_1 = "p"
    elif result_1 == 26:
        result_1 = "q"
    elif result_1 == 27:
        result_1 = "r"
    elif result_1 == 28:
        result_1 = "s"
    elif result_1 == 29:
        result_1 = "t"
    elif result_1 == 30:
        result_1 = "u"
    elif result_1 == 31:
        result_1 = "v"
    elif result_1 == 32:
        result_1 = "w"
    elif result_1 == 33:
        result_1 = "x"
    elif result_1 == 34:
        result_1 = "y"
    elif result_1 == 35:
        result_1 = "z"
    result_10 = fNum // t_formation
    print(result_10, result_1, sep = "")