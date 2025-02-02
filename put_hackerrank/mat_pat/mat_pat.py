def is_king_safe(board, king_pos):
    if "w" in board[king_pos[0]]:
        return True
    else:
        for i in range(8):
            if board[i][king_pos[1]]=="w":
                return True
    return False
def is_field_safe(board, y, x):
    for i in range(8):
        if i == y:
            continue
        elif board[i][x] == "w":
            return False
    for j in range(8):
        if j == x:
            continue
        elif board[y][j] == "w":
            return False
    return True

board = []
king_pos = []
is_check = False
for i in range(8):
    line = input()
    board.append(line)
    if "k" in line:
        king_pos = [i, line.index("k")]
# print(king_pos)
fields = [
 [-1,-1], [-1,0], [-1,+1],
 [0,-1],          [0,+1],
 [+1,-1], [+1,0], [+1, +1]]
is_check = is_king_safe(board, king_pos)
checked_fields = []
for y,x in fields:
    is_safe = True
    if king_pos[0]+y in range(8) and king_pos[1]+x in range(8):
        is_safe = is_field_safe(board, king_pos[0]+y, king_pos[1]+x)
        checked_fields.append(is_safe)
# print(checked_fields)
if is_check and True not in checked_fields:
    print("mat")
elif is_check == False and True not in checked_fields:
    print("pat")
else:
    print("game goes on")
# print(is_check)
# print(checked_fields)
