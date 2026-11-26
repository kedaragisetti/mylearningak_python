"""
Command-Line Tic-Tac-Toe Game
Player ('O') vs. Computer ('X') using a 3x3 2D list board.
"""

from random import randrange


def display_board(board):
    print("+-------" * 3, "+", sep="")

    for row in range(3):
        print("|       " * 3, "|", sep="")

        for col in range(3):
            print("|   " + str(board[row][col]) + "   ", end="")

        print("|")
        print("|       " * 3, "|", sep="")
        print("+-------" * 3, "+", sep="")


def enter_move(board):
    while True:
        move = input("Enter your move: ")

        if len(move) != 1 or move < '1' or move > '9':
            print("Bad move - repeat your input!")
            continue

        move = int(move) - 1
        row = move // 3
        col = move % 3

        if board[row][col] in ['X', 'O']:
            print("Field already occupied!")
            continue

        board[row][col] = 'O'
        break


def make_list_of_free_fields(board):
    free = []

    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X', 'O']:
                free.append((row, col))

    return free


def victory_for(board, sign):
    if sign == "X":
        who = "Computer"
    else:
        who = "You"

    for i in range(3):
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            return who

        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return who

    if board[0][0] == sign and board[1][1] == sign and board[2][2] == sign:
        return who

    if board[0][2] == sign and board[1][1] == sign and board[2][0] == sign:
        return who

    return None


def draw_move(board):
    free = make_list_of_free_fields(board)

    if len(free):
        row, col = free[randrange(len(free))]
        board[row][col] = 'X'


def play_game():
    board = [
        [1, 2, 3],
        [4, 'X', 6],
        [7, 8, 9]
    ]

    human_turn = True
    winner = None

    while True:
        display_board(board)

        if human_turn:
            enter_move(board)
            winner = victory_for(board, 'O')
        else:
            draw_move(board)
            winner = victory_for(board, 'X')

        if winner:
            break

        if len(make_list_of_free_fields(board)) == 0:
            break

        human_turn = not human_turn

    display_board(board)

    if winner:
        print(winner, "won!")
    else:
        print("Tie!")


if __name__ == "__main__":
    play_game()