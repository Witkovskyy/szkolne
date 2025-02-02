hwyx = list(map(int,input().split()))
if hwyx[0]>hwyx[2] and hwyx[1]>hwyx[3]:
    wall = []
    for i in range(hwyx[0]):
        wall.append(list(map(int,input().split())))
    # print(wall)
    for i in range(0,(hwyx[0] - hwyx[2]+1)):
        for j in range(0,(hwyx[1] - hwyx[3]+1)):
            starting_pos = [i,j]
            is_fit = True
            for k in range(i, (i+hwyx[2])):
                for l in range(j, (j+hwyx[3])):
                    # print(f"{i} {j} {k} {l}")
                    # print(wall[k][l])
                    if wall[k][l]==1:
                        is_fit = False
            if is_fit==True:
                print("True")
                break
        if is_fit==True:
            break
    if is_fit==False:
        print("False")
else:
    print("False")
