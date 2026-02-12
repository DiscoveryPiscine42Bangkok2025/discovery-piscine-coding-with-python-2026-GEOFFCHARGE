from checkmate import checkboard, checkmate

def main():
    board = """\
            R...
            .K..
            ..P.
            ....\
            """
    if checkboard(board):
        checkmate(board)

if __name__ == "__main__":
    main()
