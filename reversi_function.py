import copy


#間違ったところに石を置いた(おけない)ときに次の相手のターンに移るところがなおってない
def put_stone(x,y, who, board):
    if 1 <= x <= 8 and 1 <= y <= 8:
        if board[y-1][x-1] == 0:
            board[y-1][x-1] = who
            stone_before_change = 0
            for i in range(len(board)):
                stone_before_change += board[i].count(who)
            change_stone(x,y,who,board)
            stone_after_change = 0
            for i in range(len(board)):
                stone_after_change += board[i].count(who)
            if stone_before_change == stone_after_change:
                 board[y-1][x-1] = 0
                 print('他の石をひっくり返すことができないのでそこには置けません')
            else :
                for cell in board:
                    print(cell)
                if who == 1:
                    who = 2
                    print('次は'+str(who)+'の番です')
                else:
                    who = 1
                    print('次は'+str(who)+'の番です')
        else:
            print('そこにはすでに石が置かれています')
    else:
        print('石をおける有効な範囲(1~8)で入力してください')



def change_stone(x, y, turn, field):
    '''置いた石の右側を見る'''
    if x < 7:
        if field[y-1][x] == turn or field[y-1][x] == 0:
            pass
        else:
            if field[y-1][x+1] == turn:
                field[y-1][x] = turn
            elif field[y-1][x+1] == 0:
                pass
            else:
                if x < 6:
                    if  field[y-1][x+2] == turn:
                        field[y-1][x] = turn
                        field[y-1][x+1] = turn
                    elif field[y-1][x+2] == 0:
                        pass
                    else:
                        if x < 5:
                            if  field[y-1][x+3] == turn:
                                field[y-1][x] = turn
                                field[y-1][x+1] = turn
                                field[y-1][x+2] = turn
                            elif field[y-1][x+3] == 0:
                                pass
                            else:
                                if x < 4:
                                    if  field[y-1][x+3] == turn:
                                        field[y-1][x] = turn
                                        field[y-1][x+1] = turn
                                        field[y-1][x+2] = turn
                                        field[y-1][x+3] = turn
                                    elif field[y-1][x+3] == 0:
                                        pass
                                    else:
                                        if x < 3:
                                            if  field[y-1][x+4] == turn:
                                                field[y-1][x] = turn
                                                field[y-1][x+1] = turn
                                                field[y-1][x+2] = turn
                                                field[y-1][x+3] = turn
                                                field[y-1][x+4] = turn
                                            elif field[y-1][x+4] == 0:
                                                pass
                                            else:
                                                if x < 2:
                                                    if  field[y-1][x+5] == turn:
                                                        field[y-1][x] = turn
                                                        field[y-1][x+1] = turn
                                                        field[y-1][x+2] = turn
                                                        field[y-1][x+3] = turn
                                                        field[y-1][x+4] = turn
                                                        field[y-1][x+5] = turn
    '''置いた石の左側を見る'''
    if x > 2:
        if field[y-1][x-2] == turn or field[y-1][x-2] == 0:
            pass
        else:
            if field[y-1][x-3] == turn:
                field[y-1][x-2] = turn
            elif field[y-1][x-3] == 0:
                pass
            else:
                if x > 3:
                    if  field[y-1][x-4] == turn:
                        field[y-1][x-1] = turn
                        field[y-1][x-2] = turn
                    elif field[y-1][x-4] == 0:
                        pass
                    else:
                        if x > 4:
                            if  field[y-1][x-5] == turn:
                                field[y-1][x-1] = turn
                                field[y-1][x-2] = turn
                                field[y-1][x-3] = turn
                            elif field[y-1][x-5] == 0:
                                pass
                            else:
                                if x > 5:
                                    if  field[y-1][x-6] == turn:
                                        field[y-1][x-1] = turn
                                        field[y-1][x-2] = turn
                                        field[y-1][x-3] = turn
                                        field[y-1][x-4] = turn
                                    elif field[y-1][x-6] == 0:
                                        pass
                                    else:
                                        if x > 6:
                                            if  field[y-1][x-7] == turn:
                                                field[y-1][x-1] = turn
                                                field[y-1][x-2] = turn
                                                field[y-1][x-3] = turn
                                                field[y-1][x-4] = turn
                                                field[y-1][x-5] = turn
                                            elif field[y-1][x-7] == 0:
                                                pass
                                            else:
                                                if x > 7:
                                                    if  field[y-1][x-8] == turn:
                                                        field[y-1][x-1] = turn
                                                        field[y-1][x-2] = turn
                                                        field[y-1][x-3] = turn
                                                        field[y-1][x-4] = turn
                                                        field[y-1][x-5] = turn
                                                        field[y-1][x-6] = turn
    '''置いた石の上側を見る'''
    if y > 2:
        if field[y-2][x-1] == turn or field[y-2][x-1] == 0:
            pass
        else:
            if field[y-3][x-1] == turn:
                field[y-2][x-1] = turn
            elif field[y-3][x-1] == 0:
                pass
            else:
                if y > 3:
                    if  field[y-4][x-1] == turn:
                        field[y-1][x-1] = turn
                        field[y-2][x-1] = turn
                    elif field[y-4][x-1] == 0:
                        pass
                    else:
                        if y > 4:
                            if  field[y-5][x-1] == turn:
                                field[y-1][x-1] = turn
                                field[y-2][x-1] = turn
                                field[y-3][x-1] = turn
                            elif field[y-5][x-1] == 0:
                                pass
                            else:
                                if y > 5:
                                    if  field[y-6][x-1] == turn:
                                        field[y-1][x-1] = turn
                                        field[y-2][x-1] = turn
                                        field[y-3][x-1] = turn
                                        field[y-4][x-1] = turn
                                    elif field[y-6][x-1] == 0:
                                        pass
                                    else:
                                        if y > 6:
                                            if  field[y-7][x-1] == turn:
                                                field[y-1][x-1] = turn
                                                field[y-2][x-1] = turn
                                                field[y-3][x-1] = turn
                                                field[y-4][x-1] = turn
                                                field[y-5][x-1] = turn
                                            elif field[y-7][x-1] == 0:
                                                pass
                                            else:
                                                if y > 7:
                                                    if  field[y-8][x-1] == turn:
                                                        field[y-1][x-1] = turn
                                                        field[y-2][x-1] = turn
                                                        field[y-3][x-1] = turn
                                                        field[y-4][x-1] = turn
                                                        field[y-5][x-1] = turn
                                                        field[y-6][x-1] = turn
    '''置いた石の下側を見る'''
    if y < 7:
        if field[y][x-1] == turn or field[y][x-1] == 0:
            pass
        else:
            if field[y+1][x-1] == turn:
                field[y][x-1] = turn
            elif field[y+1][x-1] == 0:
                pass
            else:
                if y < 6:
                    if  field[y+2][x-1] == turn:
                        field[y][x-1] = turn
                        field[y+1][x-1] = turn
                    elif field[y+2][x-1] == 0:
                        pass
                    else:
                        if y < 5:
                            if  field[y+3][x-1] == turn:
                                field[y][x-1] = turn
                                field[y+1][x-1] = turn
                                field[y+2][x-1] = turn
                            elif field[y+3][x-1] == 0:
                                pass
                            else:
                                if y < 4:
                                    if  field[y+3][x-1] == turn:
                                        field[y][x-1] = turn
                                        field[y+1][x-1] = turn
                                        field[y+2][x-1] = turn
                                        field[y+3][x-1] = turn
                                    elif field[y+3][x-1] == 0:
                                        pass
                                    else:
                                        if y < 3:
                                            if  field[y+4][x-1] == turn:
                                                field[y][x-1] = turn
                                                field[y+1][x-1] = turn
                                                field[y+2][x-1] = turn
                                                field[y+3][x-1] = turn
                                                field[y+4][x-1] = turn
                                            elif field[y+4][x-1] == 0:
                                                pass
                                            else:
                                                if y < 2:
                                                    if  field[y+5][x-1] == turn:
                                                        field[y][x-1] = turn
                                                        field[y+1][x-1] = turn
                                                        field[y+2][x-1] = turn
                                                        field[y+3][x-1] = turn
                                                        field[y+4][x-1] = turn
                                                        field[y+5][x-1] = turn
    '''置いた石の左上を見る'''
    if  x > 2 and y > 2:
        if field[y-2][x-2] == turn or  field[y-2][x-2] == 0:
            pass
        else:
            if field[y-3][x-3] == turn:
                field[y-2][x-2] = turn
            elif field[y-3][x-3] == 0:
                pass
            else:
                if x > 3 and y > 3:
                     if field[y-4][x-4] == turn:
                         field[y-2][x-2] = turn
                         field[y-3][x-3] = turn
                     elif field[y-4][x-4] == 0:
                         pass
                     else:
                         if x > 4 and y > 4:
                              if field[y-5][x-5] == turn:
                                  field[y-2][x-2] = turn
                                  field[y-3][x-3] = turn
                                  field[y-4][x-4] = turn
                              elif field[y-5][x-5] == 0:
                                  pass
                              else:
                                  if x > 5 and y > 5:
                                       if field[y-6][x-6] == turn:
                                           field[y-2][x-2] = turn
                                           field[y-3][x-3] = turn
                                           field[y-4][x-4] = turn
                                           field[y-5][x-5] = turn
                                       elif field[y-6][x-6] == 0:
                                           pass
                                       else:
                                           if x > 6 and y > 6:
                                                if field[y-7][x-7] == turn:
                                                    field[y-2][x-2] = turn
                                                    field[y-3][x-3] = turn
                                                    field[y-4][x-4] = turn
                                                    field[y-5][x-5] = turn
                                                    field[y-6][x-6] = turn
                                                elif field[y-7][x-7] == 0:
                                                    pass
                                                else:
                                                    if x > 7 and y > 7:
                                                         if field[y-8][x-8] == turn:
                                                             field[y-2][x-2] = turn
                                                             field[y-3][x-3] = turn
                                                             field[y-4][x-4] = turn
                                                             field[y-5][x-5] = turn
                                                             field[y-6][x-6] = turn
                                                             field[y-7][x-7] = turn
    '''置いた石の右上を見る'''
    if  x < 7  and y > 2:
        if field[y-2][x] == turn or  field[y-2][x] == 0:
            pass
        else:
            if field[y-3][x+1] == turn:
                field[y-2][x] = turn
            elif field[y-3][x+1] == 0:
                pass
            else:
                if x < 6 and y > 3:
                     if field[y-4][x+2] == turn:
                         field[y-2][x] = turn
                         field[y-3][x+1] = turn
                     elif field[y-4][x+2] == 0:
                         pass
                     else:
                         if x < 5 and y > 4:
                              if field[y-5][x+3] == turn:
                                  field[y-2][x] = turn
                                  field[y-3][x+1] = turn
                                  field[y-4][x+2] = turn
                              elif field[y-5][x+3] == 0:
                                  pass
                              else:
                                  if x < 4 and y > 5:
                                       if field[y-6][x+4] == turn:
                                           field[y-2][x] = turn
                                           field[y-3][x+1] = turn
                                           field[y-4][x+2] = turn
                                           field[y-5][x+3] = turn
                                       elif field[y-6][x+4] == 0:
                                           pass
                                       else:
                                           if x < 3 and y > 6:
                                                if field[y-7][x+5] == turn:
                                                    field[y-2][x] = turn
                                                    field[y-3][x+1] = turn
                                                    field[y-4][x+2] = turn
                                                    field[y-5][x+3] = turn
                                                    field[y-6][x+4] = turn
                                                elif field[y-7][x+5] == 0:
                                                    pass
                                                else:
                                                    if x < 2 and y > 7:
                                                         if field[y-8][x+6] == turn:
                                                             field[y-2][x] = turn
                                                             field[y-3][x+1] = turn
                                                             field[y-4][x+2] = turn
                                                             field[y-5][x+3] = turn
                                                             field[y-6][x+4] = turn
                                                             field[y-7][x+5] = turn
    '''置いた石の左下を見る'''
    if  x > 2 and y < 7:
        if field[y][x-2] == turn or  field[y][x-2] == 0:
            pass
        else:
            if field[y+1][x-3] == turn:
                field[y][x-2] = turn
            elif field[y+1][x-3] == 0:
                pass
            else:
                if x > 3 and y < 6:
                     if field[y+2][x-4] == turn:
                         field[y][x-2] = turn
                         field[y+1][x-3] = turn
                     elif field[y+2][x-4] == 0:
                         pass
                     else:
                         if x > 4 and y < 5:
                              if field[y+3][x-5] == turn:
                                  field[y][x-2] = turn
                                  field[y+1][x-3] = turn
                                  field[y+2][x-4] = turn
                              elif field[y+3][x-5] == 0:
                                  pass
                              else:
                                  if x > 5 and y < 4:
                                       if field[y+4][x-6] == turn:
                                           field[y][x-2] = turn
                                           field[y+1][x-3] = turn
                                           field[y+2][x-4] = turn
                                           field[y+3][x-5] = turn
                                       elif field[y+4][x-6] == 0:
                                           pass
                                       else:
                                           if x > 6 and y < 3:
                                                if field[y+5][x-7] == turn:
                                                    field[y][x-2] = turn
                                                    field[y+1][x-3] = turn
                                                    field[y+2][x-4] = turn
                                                    field[y+3][x-5] = turn
                                                    field[y+4][x-6] = turn
                                                elif field[y+5][x-7] == 0:
                                                    pass
                                                else:
                                                    if x > 7 and y < 2:
                                                         if field[y+6][x-8] == turn:
                                                             field[y][x-2] = turn
                                                             field[y+1][x-3] = turn
                                                             field[y+2][x-4] = turn
                                                             field[y+3][x-5] = turn
                                                             field[y+4][x-6] = turn
                                                             field[y+5][x-7] = turn
    '''置いた石の右下を見る'''
    if  x < 7 and y < 7:
        if field[y][x] == turn or  field[y][x] == 0:
            pass
        else:
            if field[y+1][x+1] == turn:
                field[y][x] = turn
            elif field[y+1][x+2] == 0:
                pass
            else:
                if x < 6 and y < 6:
                     if field[y+2][x+2] == turn:
                         field[y][x] = turn
                         field[y+1][x+1] = turn
                     elif field[y+2][x+2] == 0:
                         pass
                     else:
                         if x < 5 and y < 5:
                              if field[y+3][x+3] == turn:
                                  field[y][x] = turn
                                  field[y+1][x+1] = turn
                                  field[y+2][x+2] = turn
                              elif field[y+3][x+3] == 0:
                                  pass
                              else:
                                  if x <4 and y < 4:
                                       if field[y+4][x+4] == turn:
                                           field[y][x] = turn
                                           field[y+1][x+1] = turn
                                           field[y+2][x+2] = turn
                                           field[y+3][x+3] = turn
                                       elif field[y+4][x+4] == 0:
                                           pass
                                       else:
                                           if x < 3 and y < 3:
                                                if field[y+5][x+5] == turn:
                                                    field[y][x] = turn
                                                    field[y+1][x+1] = turn
                                                    field[y+2][x+2] = turn
                                                    field[y+3][x+3] = turn
                                                    field[y+4][x+4] = turn
                                                elif field[y+5][x+5] == 0:
                                                    pass
                                                else:
                                                    if x < 2 and y < 2:
                                                         if field[y+6][x+6] == turn:
                                                             field[y][x] = turn
                                                             field[y+1][x+1] = turn
                                                             field[y+2][x+2] = turn
                                                             field[y+3][x+3] = turn
                                                             field[y+4][x+4] = turn
                                                             field[y+5][x+5] = turn


def show_put_point(turn,board):
    enable_point = []
    for i in range(len(board)):
        for k in range(len(board[i])):
            if board[i][k] == 0:
                board_copy = copy.deepcopy(board)
                board_copy[i][k] = turn
                stone_before_change = 0
                for l in range(len(board_copy)):
                    stone_before_change += board_copy[l].count(turn)
                change_stone(k+1,i+1,turn,board_copy)
                stone_after_change = 0
                for l in range(len(board_copy)):
                    stone_after_change += board_copy[l].count(turn)
                if stone_before_change == stone_after_change:
                    pass
                else:
                    enable_point.append([k+1, i+1])
    if len(enable_point) == 0:
        print(str(turn) + 'を置けるところはありません')
    else:
        print(str(turn) + 'を置ける場所は以下の座標です')
        for i in enable_point:
            print(i)

def check_end(turn,board):#両者が置ける場所がなくなったかどうか、つまり勝負が終わったかを判定します
    enable_point = []
    for i in range(len(board)):
        for k in range(len(board[i])):
            if board[i][k] == 0:
                board_copy = copy.deepcopy(board)
                board_copy[i][k] = turn
                stone_before_change = 0
                for l in range(len(board_copy)):
                    stone_before_change += board_copy[l].count(turn)
                change_stone(k+1,i+1,turn,board_copy)
                stone_after_change = 0
                for l in range(len(board_copy)):
                    stone_after_change += board_copy[l].count(turn)
                if stone_before_change == stone_after_change:
                    pass
                else:
                    enable_point.append([k+1, i+1])
    if len(enable_point) == 0:
        if turn == 1:
            enable_point = []
            for i in range(len(board)):
                for k in range(len(board[i])):
                    if board[i][k] == 0:
                        board_copy = copy.deepcopy(board)
                        board_copy[i][k] = 2
                        stone_before_change = 0
                        for l in range(len(board_copy)):
                            stone_before_change += board_copy[l].count(2)
                        change_stone(k+1,i+1,board_copy)
                        stone_after_change = 0
                        for l in range(len(board_copy)):
                            stone_after_change += board_copy[l].count(2)
                        if stone_before_change == stone_after_change:
                            pass
                        else:
                            enable_point.append([k+1, i+1])
            if len(enable_point) == 0:
                return False
            else:
                return True
        elif turn == 2:
            enable_point = []
            for i in range(len(board)):
                for k in range(len(board[i])):
                    if board[i][k] == 0:
                        board_copy = copy.deepcopy(board)
                        board_copy[i][k] = 1
                        stone_before_change = 0
                        for l in range(len(board_copy)):
                            stone_before_change += board_copy[l].count(1)
                        change_stone(k+1,i+1,turn,board_copy)
                        stone_after_change = 0
                        for l in range(len(board_copy)):
                            stone_after_change += board_copy[l].count(1)
                        if stone_before_change == stone_after_change:
                            pass
                        else:
                            enable_point.append([k+1, i+1])
            if len(enable_point) == 0:
                return False
            else:
                return True
    else:
        return True

def check_winner(board):
    board_copy = copy.deepcopy(board)
    count1 = 0
    count2 = 0
    for i in range(len(board_copy)):
        count1 += board_copy[i].count(1)
        count2 += board_copy[i].count(2)
    if count1 > count2:
        print('プレイヤー1の勝ちです')
    elif count1 < count2:
        print('プレイヤー2の勝ちです')
    else:
        print('このゲームは引き分けです')
        
        
