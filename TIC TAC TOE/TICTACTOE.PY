# Tic-Tac-Toe using Minimax Algorithm
# Human = X
# AI = O

board = [" " for _ in range(9)]


def display():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()


def winner(player):
    combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in combinations:
        if board[a] == board[b] == board[c] == player:
            return True
    return False


def minimax(is_maximizing):
    if winner("O"):
        return 1

    if winner("X"):
        return -1

    if " " not in board:
        return 0

    if is_maximizing:
        best_score = -1000

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:
        best_score = 1000

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score


def ai_move():
    best_score = -1000
    best_move = 0

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(False)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"


# Main program
print("TIC-TAC-TOE")
print("You are X")
print("AI is O")

while True:
    display()

    # Human move
    move = int(input("Enter position (1-9): ")) - 1

    if move < 0 or move > 8 or board[move] != " ":
        print("Invalid move!")
        continue

    board[move] = "X"

    if winner("X"):
        display()
        print("You WIN!")
        break

    if " " not in board:
        display()
        print("DRAW!")
        break

    # AI move
    print("AI is thinking...")
    ai_move()

    if winner("O"):
        display()
        print("AI WINS!")
        break
