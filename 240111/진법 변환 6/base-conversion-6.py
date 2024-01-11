formation, fNum, t_formation = map(int, input().split())
fNum = str(fNum)
if formation != 10:
    fNum = int(fNum, formation)


result_1 = fNum % t_formation
result_10 = fNum // t_formation

print(result_10, result_1, sep = "")