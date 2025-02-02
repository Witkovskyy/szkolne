def reverse_row(matrix, x, n, m): # m = rows, n = cols
    temp_arr = []
    if n < m:
        for i in range(0, len(matrix[x])):
            temp_arr.append(matrix[x][i])
        j = 0
        for i in range(len(matrix[x])-1, -1, -1):
            matrix[x][i] = temp_arr[j]
            j = j + 1
    else:
        for i in range(0, len(matrix[x])):
            temp_arr.append(matrix[x][i])
        j = 0
        for i in range(len(matrix[x])-1, -1, -1):
            matrix[x][i] = temp_arr[j]
            j = j + 1

    # matrix[x] = matrix[x][::-1]
    return(matrix)

def reverse_col(matrix, n, m, x):
    if x > len(matrix[0]):
        return(matrix)
    temp_rev = []
    if m<n:
        for i in range(m-1, -1, -1):
            temp_rev.append(matrix[i][x])
        for i in range(0, m):
            matrix[i][x] = temp_rev[i]
    else:
        for i in range(n-1, -1, -1):
            temp_rev.append(matrix[i][x])
        for i in range(0, n):
            matrix[i][x] = temp_rev[i]

    return(matrix)

def transpose(matrix, n, m):
    new_matrix = []
    if n<=m:
        for i in range(0, n):
            temp_arr = []
            for j in range(0, m):
                temp_arr.append(matrix[j][i])
            new_matrix.append(temp_arr)
    else:
        for i in range(0, m):
            temp_arr = []
            for j in range(0, n):
                temp_arr.append(matrix[i][j])
            new_matrix.append(temp_arr)
    temp = m
    m = n
    n = temp        
    return(new_matrix, n, m)

def custom_int(value):
    result = 0
    for char in value:
        result = result * 10 + (ord(char) - ord('0'))
    return result

def custom_split(input_string, delimiter=" "):
    result = []
    current = ""
    for char in input_string:
        if char == delimiter:
            if current != "":
                result.append(current)
                current = ""
        else:
            current += char
    if current != "":
        result.append(current)
    return result

[m, n] = custom_split(input())
n = custom_int(n)
m = custom_int(m)
if n!=0 and m!=0:
    matrix = []
    for i in range(0, m):
        temp_arr = []
        temp_str = input()
        temp_arr = custom_split(temp_str.strip())
        for i in range(0, len(temp_arr)):
            temp_arr[i] = custom_int(temp_arr[i])
        matrix.append(temp_arr)
    k = custom_int(input())
    if k!=0:
        for i in range(0, k):
            operation = input()
            if len(operation)>1:
                s, x = custom_split(operation.strip())
                x = custom_int(x)
                if x == n or x == m:
                    x = x - 1
                if s=="RR":
                    matrix = reverse_row(matrix, x, n, m)
                elif s=="RC":
                    matrix = reverse_col(matrix, n, m, x)
            elif operation=="T":
                new_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
                del(matrix)
                matrix = []
                for i in range(0,len(new_matrix)):
                    temp_arr = []
                    for j in range(len(new_matrix[0])):
                        temp_arr.append(new_matrix[i][j])
                    matrix.append(temp_arr)

                # matrix, n, m = transpose(matrix, n, m)
                # print(matrix)
                    # new_matrix = []
                    # if n<=m:
                    #     for i in range(0, len(matrix)):
                    #         temp_arr = []
                    #         for j in range(0, len(matrix[0])):
                    #             temp_arr.append(matrix[j][i])
                    #         new_matrix.append(temp_arr)
                    # else:
                    #     for i in range(0, len(matrix[0])):
                    #         temp_arr = []
                    #         for j in range(0, len(matrix)):
                    #             temp_arr.append(matrix[i][j])
                    #         new_matrix.append(temp_arr)
                    # temp = m
                    # m = n
                    # n = temp 
                    # del(matrix)
                    # matrix = new_matrix       


# aaa
        for i in range(0, m):
                for j in range(0, len(matrix[0])):
                    print(matrix[i][j], end=" ")
                print()
    
                