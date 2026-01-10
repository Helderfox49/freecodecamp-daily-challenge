def tic_tac_toe(board):
    if check_win(board, elt="X"):
        return "X wins"
    elif check_win(board, elt="O"):
        return "O wins"
    else:
        return "Draw"

def horizontal_check(board, row, elt):
    for i in range(3):
        if board[row][i] != elt:
            return False
    return True


def vertical_check(board, column, elt):
    for i in range(3):
        if board[i][column] != elt:
            return False
    return True


def diagonal_check_sup(board, elt):
    for i in range(3):
        if(board[i][i] != elt):
            return False
    return True


def diagonal_check_inf(board, elt):
    for i in range(3):
        if (board[i][2-i] != elt):
            return False
    return True


def check_win(board, elt):
    if any(horizontal_check(board, i, elt) for i in range(3)):
        return True
    
    if any(vertical_check(board, i, elt) for i in range(3)):
        return True
    
    if diagonal_check_inf(board, elt):
        return True
    
    if diagonal_check_sup(board, elt):
        return True 

    return False

if __name__ == "__main__":
    print(tic_tac_toe([["X", "X", "X"], ["O", "O", "X"], ["O", "X", "O"]]))
    print(tic_tac_toe([["X", "O", "X"], ["X", "O", "X"], ["O", "O", "X"]]))
    print(tic_tac_toe([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "O"]]))
    print(tic_tac_toe([["X", "X", "O"], ["X", "O", "X"], ["O", "X", "X"]]))

    print(tic_tac_toe([["X", "O", "O"], ["O", "X", "O"], ["O", "X", "X"]]))
    print(tic_tac_toe([["O", "X", "X"], ["X", "O", "O"], ["X", "O", "X"]]))
