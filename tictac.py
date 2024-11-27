import random

# Definimos el tablero
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Comprobar filas, columnas y diagonales
    for row in board:
        if row.count(row[0]) == 3 and row[0] != " ":
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    return None

def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def minimax(board, depth, is_maximizing):
    score = check_winner(board)
    
    if score == "O":  # Máquina
        return 1
    elif score == "X":  # Jugador
        return -1
    elif is_full(board):
        return 0
    
    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def best_move(board):
    best_score = -float('inf')
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, 0, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    print("¡Bienvenido al Tic Tac Toe!")
    print_board(board)

    while True:
        # Turno del jugador
        while True:
            try:
                row = int(input("Elige la fila (0, 1, 2): "))
                col = int(input("Elige la columna (0, 1, 2): "))
                if board[row][col] == " ":
                    board[row][col] = "X"
                    break
                else:
                    print("Esa posición ya está ocupada. Intenta de nuevo.")
            except (ValueError, IndexError):
                print("Entrada no válida. Por favor, elige números entre 0 y 2.")

        print_board(board)
        if check_winner(board) == "X":
            print("¡Felicidades, ganaste!")
            break
        if is_full(board):
            print("¡Es un empate!")
            break

        # Turno de la máquina
        print("Turno de la máquina:")
        row, col = best_move(board)
        board[row][col] = "O"
        print_board(board)
        if check_winner(board) == "O":
            print("La máquina ganó. ¡Intenta de nuevo!")
            break
        if is_full(board):
            print("¡Es un empate!")
            break

if __name__ == "__main__":
    play_game()