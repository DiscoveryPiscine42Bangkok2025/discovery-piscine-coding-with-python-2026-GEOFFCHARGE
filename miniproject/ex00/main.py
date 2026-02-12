from checkmate import checkboard, checkmate

def main():
    board = """\
            P...
            .K..
            ....
            ....\
            """
    if checkboard(board):
        checkmate(board)

if __name__ == "__main__":
    main()
