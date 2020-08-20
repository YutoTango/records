import reversi_function as rv
import copy

size =8
board = [[0 for i in range(size)] for i in range(size)]
board[4][3] = 2
board[3][4] = 2
board[4][4] = 1
board[3][3] = 1
turn = 1

for cell in board:
    print(cell)
while rv.check_end(turn,board):
    rv.show_put_point(turn,board)
    x = int(input('プレイヤー' + str(turn) + 'は石を置くx座標を入力してください：'))
    y = int(input('プレイヤー' + str(turn) + 'は石を置くy座標を入力してください：'))
    rv.put_stone(x,y,turn,board)
    if turn == 1:
        turn = 2
    else:
        turn = 1
rv.check_winner(board)
