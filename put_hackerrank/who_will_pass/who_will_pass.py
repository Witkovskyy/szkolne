n = int(input())
# matrix = [[list(map(int,input())) for i in range (n)] for j in range(n)]
matrix = []
for i in range(n):
    line = list(map(int, input().split()))
    matrix.append(line)
printout_matrix=[]
neighbours =[
 [-1,-1], [-1,0], [-1,+1],
 [0,-1],          [0,+1],
 [+1,-1], [+1,0], [+1, +1]]

for i in range(n):
    temp_arr = []
    for j in range(n):
        if matrix[i][j]>=7:
            temp_arr.append(1)
        else:
            neighbour_sum = 0
            neighbour_count = 0
            for y,x in neighbours:
                if i+y in range(n) and j+x in range(n):
                    neighbour_count +=1
                    neighbour_sum += matrix[i+y][j+x]
            avg = neighbour_sum/neighbour_count
            if avg>=3:
                temp_arr.append(1)
            else:
                temp_arr.append(0)
    printout_matrix.append(temp_arr)
for i in range(n):
    for j in range(n):
        print(printout_matrix[i][j], end=" ")
    print()
    

            
