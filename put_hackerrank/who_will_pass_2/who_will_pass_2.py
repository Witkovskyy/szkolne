n = int(input())
# matrix = [[list(map(int,input())) for i in range (n)] for j in range(n)]
matrix = []
for i in range(n):
    line = list(map(int, input().split()))
    matrix.append(line)
printout_matrix=[]
# neighbours =[
#  [-1,-1], [-1,0], [-1,+1],
#  [0,-1],          [0,+1],
#  [+1,-1], [+1,0], [+1, +1]]

for i in range(n):
    temp_arr = []
    for j in range(n):
        if matrix[i][j]>=7:
            temp_arr.append(1)
        else:
            neighbour_sum = 0
            neighbour_count = 0
            for k in range(n):
                    if matrix[i][j]<=matrix[i][k]:
                        neighbour_count +=1
                        neighbour_sum += matrix[i][k]
            for k in range(n):
                if k==i:
                    continue
                elif matrix[i][j]<=matrix[k][j]:
                    neighbour_count +=1
                    neighbour_sum += matrix[k][j]
            avg = neighbour_sum/neighbour_count
            if avg>=7:
                temp_arr.append(1)
            else:
                temp_arr.append(0)
    printout_matrix.append(temp_arr)
for i in range(n):
    for j in range(n):
        print(printout_matrix[i][j], end=" ")
    print()
    

            
