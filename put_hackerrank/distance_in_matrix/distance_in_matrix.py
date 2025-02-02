def find_smallest(matrix,y,x,n):
    min_min,distance = 1001,float("inf")
    for i in range(n):
        for j in range(n):
            if i==y and j==x:
                continue
            elif matrix[i][j]==1:
                if (i+1)%(y+1)==0 and (j+1)%(x+1)==0:
                    distance = abs((y+1)-(i+1))+abs((x+1)-(j+1))
                    # print(f"{distance} {j}")
                else:
                    distance = 1000
                if distance<min_min:
                    min_min=distance
    return min_min




n = int(input())
matrix = []
for i in range(n):
    temp_arr = (list(map(int, input().split())))
    matrix.append(temp_arr)
min_distance = float('inf')
temp_smallest = float('inf')
for i in range(n):
    for j in range(n):
        if matrix[i][j]==1:
            temp_smallest = find_smallest(matrix,i,j,n)
            # print(temp_smallest)
        if temp_smallest<min_distance:
            # print(temp_smallest)
            # print(min_distance)
            # print(temp_smallest<min_distance)
            min_distance=temp_smallest
        # print(min_distance)

print(min_distance)