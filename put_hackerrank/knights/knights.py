n = int(input())
board = []
for i in range(n):
    line = input()
    board.append(line)
moves = [
  [-1,-2] ,[-2,-1], [-2,+1], [-1,+2],
  [+1,-2], [+2,-1], [+2,+1], [+1, +2]
]
total_attacks = 0
for i in range(n):
    for j in range(n):
        if board[i][j]=='s':
            for y,x in moves:
                if y+i in range(n) and x+j in range(n):
                    if board[y+i][x+j]=='s':
                        total_attacks+=1
print(total_attacks)