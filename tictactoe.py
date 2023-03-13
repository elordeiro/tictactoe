import random
import time

CLEAR = "\033[2J"
RETURN = "\033[H"
start_time = time.time()

board = ["   "] * 9

def printBoard(start_time):
    for i in range(3):
        for j in range(3):
            if j < 2:
                print(" " + str(i * 3 + j + 1) + " |", end="")
            else:
                print(" " + str(i * 3 + j + 1))
        if i < 2:
            print("-----------")
    print("###########")
    for i in range(3):
        for j in range(3):
            if j < 2:
                print(board[i * 3 + j] + "|", end="")
            else:
                print(board[i * 3 + j])
        if i < 2:
            print("-----------")
    if start_time > 0:
        print(f"Best move reached in {round((time.time() - start_time), 5)}s")

def getUserInput():
    while True:
        userInput = int(input("Please enter a square:   ")) - 1
        if 0 <= userInput < 9 and board[userInput] == "   ":
            board[userInput] = " X "
            break
        else:
            print("Invalid Input")

def possible_moves(board):
    moves = []
    for i, pos in enumerate(board):
        if pos == "   ":
            moves.append(i)
    return moves

def minimax(board, depth, maximizingPlayer):
    node = gameOver(board)
    if node == " O ":
        return -10
    elif node == " X ":
        return 10
    elif node == "Draw":
        return 0
    
    if maximizingPlayer:
        best_score = -float("inf")
        for move in possible_moves(board):
            board[move] = " X "
            score = minimax(board, (depth + 1), False)
            board[move] = "   "
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for move in possible_moves(board):
            board[move] = " O "
            score = minimax(board, (depth + 1), True)
            board[move] = "   "
            best_score = min(best_score, score)
        return best_score

def getCompInput():
    best_score = float("inf")
    best_move = None
    for move in possible_moves(board):
        board[move] = " O "
        score = minimax(board, 0, True)
        board[move] = "   "
        if score < best_score:
            best_score = score
            best_move = move

    board[best_move] = " O "

def win(letter):
    print(CLEAR + RETURN)
    if letter == "Draw":
        print(" -----------")
        print(f"|  Draw !!! |")
        print(" -----------\n")
    else:
        print(" -----------")
        print(f"|{letter}Wins!!! |")
        print(" -----------\n")

def gameOver(boardState):
    rows = [boardState[(i*3):(i*3)+3] for i in range(3)]
    for row in rows:                                                        # Check rows for winner
        if all(spot == row[0] and row[0] != "   " for spot in row):
            return row[0]

    cols = [[boardState[i] for i in range(j, 9, 3)] for j in range(3)]
    for col in cols:                                                        # Check cols for winner
        if all(spot == col[0] and col[0] != "   " for spot in col):
            return col[0]

    diag1 = [boardState[i] for i in [0, 4, 8]]
    if all(spot == diag1[0] and diag1[0] != "   " for spot in diag1):       # Check negative diagonal for winner
            return diag1[0]
    
    diag2 = [boardState[i] for i in [2, 4, 6]]
    if all(spot == diag2[0] and diag2[0] != "   " for spot in diag2):       # Check positive diagonal for winner
            return diag2[0]
    
    if not possible_moves(board):
        return "Draw"
    
    return False

def fakeThinking():
    waitTime = random.random()
    str = "Thinking"
    print("Thinking", end="")
    for i in range(3):
        print(CLEAR + RETURN)
        printBoard(0)
        str += "."
        print(str)
        time.sleep(waitTime)


def main():
    quit = False
    while not quit:
        start_time = 0
        while True:
            print(CLEAR + RETURN)
            printBoard(start_time)
            getUserInput()
            if gameOver(board) or not possible_moves(board):
                win(gameOver(board))
                printBoard(0)
                break
            # fakeThinking()
            start_time = time.time()
            getCompInput()
            if gameOver(board) or not possible_moves(board):
                win(gameOver(board))
                printBoard(0)
                break
        stdin = input("\nWould you like to play again?\nType y for yes\nType n for no\n---> ")
        if stdin == 'n':
            quit = True
        for i in range(9):
            board[i] = "   "
    
    print("Thank you for playing!!!")
main()