"""check"""



def checkboard(board):
    array = board.split()
    f_line = len(array[0]) # base แถวแรก
    chess = {"P": 0 ,"B":0 , "R":0,"Q":0,"K":0} # check chess
    if len(array) != f_line:
        print("it not square ")
        return 0
    for row in array:
        # print(row)
        if len(row) != f_line:
            print("it not square ")
            return 0
        
        for col in row:
            # print(col)
            if col in chess:
                chess[col] += 1
            elif col != '.':
                print("Wrong Format")
                return 0
    
    # print(chess)

    if chess["K"] > 1 or chess["Q"] > 1 or chess["B"] > 2 or chess["R"] > 2 or chess["P"] > 8:
        print("Wrong Format")
        return 0
    if chess["K"] == 0:
        print("No King?")
        return 0
    if chess["Q"] == 0 and chess["B"] == 0 and chess["R"] == 0 and chess["P"] == 0:
        print("You Don't Have Enemy?")
        return 0
    return 1

def checkmate(board):
    array = board.split()
    long = len(array[0])
    king_x,king_y = 0,0
    # i = y j = x
    is_success = 0
    
    for i in range(0,len(array)-1):
        for j in range(0,len(array[i])):
            if array[i][j] == 'K' :
                king_x,king_y = j,i

    for i in range(0,len(array)):
        for j in range(0,len(array[i])):
            if array[i][j] == 'P':
                if pow_case(king_x,king_y,[j,i]):
                    is_success = 1
                    return
            if array[i][j] == 'B':
                if bis_case(king_x,king_y,[j,i],long+1):
                    is_success = 1
                    return
            if array[i][j] == 'R':
                if rook_case(king_x,king_y,[j,i],long+1):
                    is_success = 1
                    return
            if array[i][j] == 'Q':
                if queen_case(king_x,king_y,[j,i],long+1):
                    is_success = 1
                    return
    if not is_success:
        print("Fail")
    # print(king_x,king_y)

def pow_case(king_x,king_y,enemy):
    if((enemy[0]-1,enemy[1]-1) == (king_x,king_y)) or \
        ((enemy[0]+1,enemy[1]-1) == (king_x,king_y)):
        print("Success")
        return 1

def bis_case(king_x,king_y,enemy,long):
    for i in range(1,long):
        # print((enemy[0]+i,enemy[1]+i) == (king_x,king_y))
        if ((enemy[0]-i,enemy[1]-i) == (king_x,king_y)) or\
           ((enemy[0]+i,enemy[1]+i) == (king_x,king_y)) or\
           ((enemy[0]+i,enemy[1]-i) == (king_x,king_y)) or\
            ((enemy[0]-i,enemy[1]+i) == (king_x,king_y)):
            print("Success")
            return 1
        
def rook_case(king_x,king_y,enemy,long):
    for j in range(1,long):
        # print((enemy[0],enemy[1]-j) == (king_x,king_y))
        if ((enemy[0]+j,enemy[1]) == (king_x,king_y)) or\
        ((enemy[0]-j,enemy[1]) == (king_x,king_y)) or\
        ((enemy[0],enemy[1]+j) == (king_x,king_y)) or\
        ((enemy[0],enemy[1]-j) == (king_x,king_y)):
            print("Success")
            return 1
        
def queen_case(king_x,king_y,enemy,long):
    if rook_case(king_x,king_y,[enemy[0],enemy[1]],long) or bis_case(king_x,king_y,[enemy[0],enemy[1]],long):
        # print("Success")
        return 1