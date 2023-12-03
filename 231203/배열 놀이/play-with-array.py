n, q = map(int, input().split())
nlist = list(map(int, input().split()))
qlist = list()

for i in range(q):
    templist = list(map(int, input().split()))
    qlist.append(templist)


for i in qlist:
    if i[0] == 1:
        print(i[1])
        continue
    elif i[0] == 2:          
        if i[1] in nlist:
            print(nlist.index(i[1]) + 1)
        else:
            print(0)
        continue
    elif i[0] == 3:
        for j in range(i[1]-1, i[2]):
            print(nlist[j], end = " ")
        continue
    #print(i)
    # if len(i) == 3:
    #     if i[0] == 3:
    #         for k in range(i[1], i[2]+1):
    #             print(nlist[k], end=' ')
    # elif len(i) == 2:           
    #     for j in i:   
    #         if i[0] == 1:
    #             print(nlist[i[1]])
    #         elif i[0] == 2:
    #             if j == i[1]:
    #                 print(nlist.index(i[1]))
    #             else:
    #                 print(0)
        


        # if len(i) == 2:
            
        # if len(i) == 3:

# for i in range(0, q * 2, 2):

#     if qlist[i] == 1:
#         print(nlist[qlist[i]])
#     elif qlist[i] == 2:
#         for i in nlist:
#             if i == qlist[i+1]:
#                 print(nlist.index(qlist[i+1]))
#             else:
#                 print(0)
#     elif qlist[i] == 3: