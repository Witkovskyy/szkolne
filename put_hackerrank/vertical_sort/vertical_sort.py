def wez_kolumne(matrix, col, amount_of_rows):
    arr = []
    for k in range(amount_of_rows):
        arr.append(matrix[k][col])
    return(arr)

def nadpisuj_funkcja(matrix, amount_of_rows, amount_of_cols):
    for col in range(amount_of_cols):
        arr = []
        arr = wez_kolumne(matrix,col,amount_of_rows)
        arr.sort()
        for row in range(amount_of_rows):
            matrix[row][col] = arr[row]
    return(matrix)

amount_of_cols, amount_of_rows = list(map(int,input().strip().split()))
matrix = []
for i in range(amount_of_rows):
    line = list(map(int, input().split()))
    matrix.append(line)
# print(matrix)
matrix = nadpisuj_funkcja(matrix, amount_of_rows, amount_of_cols)
for i in range(amount_of_rows):
    for j in range(amount_of_cols):
        print(matrix[i][j], end=" ")
    print()


    # n = wiersz
    # m = kolumna