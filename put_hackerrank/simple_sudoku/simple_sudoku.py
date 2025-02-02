sudoku_matrix = []
is_sudoku, diag_1, diag_2 = True, True, True
for i in range(9):
    temp_arr = []
    line = list(map(int,input().strip().split()))
    sudoku_matrix.append(line)
# print(sudoku_matrix)
for i in range(9):
    sudoku_digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for j in range(9):
        if sudoku_matrix[i][j] in sudoku_digits:
            sudoku_digits.remove(sudoku_matrix[i][j])
        else:
            is_sudoku = False
for j in range(9):
    sudoku_digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9):
        if sudoku_matrix[i][j] in sudoku_digits:
            sudoku_digits.remove(sudoku_matrix[i][j])
        else:
            is_sudoku = False

sudoku_digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(9):
    j = i
    # print(sudoku_matrix[i][j])
    if sudoku_matrix[i][j] in sudoku_digits:
            sudoku_digits.remove(sudoku_matrix[i][j])
    else:
        diag_1 = False

sudoku_digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(8, -1, -1):
    j = 8-i
    # print(sudoku_matrix[j][i])
    if sudoku_matrix[j][i] in sudoku_digits:
            sudoku_digits.remove(sudoku_matrix[j][i])
    else:
        diag_2 = False
if is_sudoku and diag_1 and diag_2:
     print("X")
elif is_sudoku:
     print("True")
else: 
     print("False")
    