#TIC TAC TOE

board = {"top-l":" ","top-m":" ","top-r":" ",
         "mid-l":" ","mid-m":" ","mid-r":" ",
         "low-l":" ","low-m":" ","low-r":" "}

def printBoard(board):
    return (f"""
     {board["top-l"]} | {board["top-m"]} | {board["top-r"]}
    ---+---+---
     {board["mid-l"]} | {board["mid-m"]} | {board["mid-r"]}
    ---+---+---
     {board["low-l"]} | {board["low-m"]} | {board["low-r"]}""")

def playGame(board):
    turn = "X"
    for i in range(9):
        print(printBoard(board))
        move = input(f"What's your move? {turn}'s turn\n=> ")
        
        if board[move] != " ":
            print("Invalid Move!")
            move = input("Enter new move:\n=> ")
        else:
            board[move] = turn
            if turn == "X":
                turn = "0"
            elif turn == "0":
                turn = "X"

    return board

playGame(board)
