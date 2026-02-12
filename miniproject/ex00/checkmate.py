def checkboard(board):
    array = board.split()
    width = len(array[0])
    chess = {"P": 0, "B": 0, "R": 0, "Q": 0, "K": 0}
    if len(array) != width:
        print("Error")
        return 0
    for row in array:
        if len(row) != width:
            print("Error")
            return 0
        for col in row:
            if col in chess:
                chess[col] += 1
            elif col != '.':
                print("Error")
                return 0
    if chess["K"] > 1 or chess["Q"] > 1 or chess["B"] > 2 or chess["R"] > 2 or chess["P"] > 8:
        print("Error")
        return 0
    if not chess["K"] or (not chess["Q"] and not chess["B"] and not chess["R"] and not chess["P"]):
        print("Error")
        return 0
    return 1

def checkmate(board):
    array = board.split()
    width = len(array[0])
    kingx, kingy = 0, 0
    for y in range(len(array)):
        for x in range(len(array[y])):
            if array[y][x] == 'K' :
                kingx, kingy = x, y
    for y in range(len(array)):
        for x in range(len(array[y])):
            piece = array[y][x]
            if piece == 'P' and pawn_case(kingx, kingy, [x, y]):
                print("Success")
                return
            if piece == 'B' and bishop_case(kingx, kingy, [x, y], width + 1):
                print("Success")
                return
            if piece == 'R' and rook_case(kingx, kingy, [x, y], width + 1):
                print("Success")
                return
            if piece == 'Q' and queen_case(kingx, kingy, [x, y], width + 1):
                print("Success")
                return
    print("Fail")

def pawn_case(kingx, kingy, enemy):
    if ((enemy[0] - 1, enemy[1] - 1) == (kingx, kingy)) or ((enemy[0] + 1, enemy[1] - 1) == (kingx, kingy)):
        return 1
    return 0

def bishop_case(kingx, kingy, enemy, width):
    for i in range(1, width):
        if ((enemy[0] - i, enemy[1] - i) == (kingx, kingy)) or ((enemy[0] + i, enemy[1] + i) == (kingx, kingy)) or\
            ((enemy[0] + i, enemy[1] - i) == (kingx, kingy)) or ((enemy[0] - i, enemy[1] + i) == (kingx, kingy)):
            return 1
    return 0

def rook_case(kingx, kingy, enemy, width):
    for j in range(1, width):
        if ((enemy[0] + j, enemy[1]) == (kingx, kingy)) or ((enemy[0] - j, enemy[1]) == (kingx, kingy)) or\
            ((enemy[0], enemy[1] + j) == (kingx, kingy)) or ((enemy[0], enemy[1] - j) == (kingx, kingy)):
            return 1
    return 0

def queen_case(kingx, kingy, enemy, width):
    if rook_case(kingx, kingy, [enemy[0], enemy[1]], width) or bishop_case(kingx, kingy, [enemy[0], enemy[1]], width):
        return 1
    return 0
