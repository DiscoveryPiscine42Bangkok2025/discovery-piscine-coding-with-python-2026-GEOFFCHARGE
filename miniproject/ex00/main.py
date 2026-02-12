"""sss"""
import sys
from checkmate import checkboard,checkmate

def main():
    # test 5*5
    board = """\
        .....
        ..K..
        .P...
        ...B.
        .....
    """
    if checkboard(board):
        checkmate(board)


if __name__ == "__main__":
    main()
# exe