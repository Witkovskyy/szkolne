def cross(matrix, big_n, n, y, x):

    cross_matrix_rows,cross_matrix_cols = [], []

    for i in range(y,(y+n)):
        temp_matrix = []
        for j in range(x,(x+n)):
            temp_matrix.append(matrix[i][j])
        cross_matrix_rows.append(temp_matrix)

    for i in range(y,(y+n)):
        temp_matrix = []
        for j in range(x,(x+n)):
            temp_matrix.append(matrix[j][i])
        cross_matrix_cols.append(temp_matrix)
    
   
    cross_sum = 0
    for item in cross_matrix_rows:
        for second_item in cross_matrix_cols:
            for i in range(len(item)):
                cross_sum += (item[i]*second_item[i])
    return cross_sum



            
            
    # print(cross_matrix_rows)
    # print(cross_matrix_cols)
    # print(cross_sum)

 

    


big_n,n = map(int,input().split())
matrix = []
max_cross = float('-inf')
for i in range(big_n):
    matrix.append(list(map(int,input().split())))
for i in range((big_n-n)):
    for j in range((big_n-n)):
        cross_product = cross(matrix, big_n, n, i, j)
        if cross_product>max_cross:
            max_cross=cross_product
print(max_cross)
