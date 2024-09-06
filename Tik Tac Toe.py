import random

logo = """

.------..------..------.       .------..------..------.       .------..------..------.
|T.--. ||I.--. ||K.--. | .-.   |T.--. ||A.--. ||C.--. | .-.   |T.--. ||O.--. ||E.--. |
| :/\: || (\/) || :/\: |((5))  | :/\: || (\/) || :/\: |((5))  | :/\: || :/\: || (\/) |
| (__) || :\/: || :\/: | '-.-. | (__) || :\/: || :\/: | '-.-. | (__) || :\/: || :\/: |
| '--'T|| '--'I|| '--'K|  ((1))| '--'T|| '--'A|| '--'C|  ((1))| '--'T|| '--'O|| '--'E|
`------'`------'`------'   '-' `------'`------'`------'   '-' `------'`------'`------'

"""

print(logo)   

# tik tak toe game

print("Welcome to a Tik Tac Toe game")

def print_board (board):
  for row in board:
    print(" | ".join(row))
    print("-" * 5)

def check_winner (board, player):
  for row in board:
    if all(s == player for s in row):
      return True

  for col in range(3):
    if all (row[col] == player for row in board):
      return True

  if all(board[i][i] == player for i in range (3)) or all(board[i][ 2-i ] == player for i in range (3)):
      return True
  return False

def is_full(board):
  return all(all(cell != " " for cell in row) for row in board)

def tik_tak_toe():
  board = [[" " for _ in range (3)] for _ in range (3)]
  current_player = "X"

  while True:
    print_board(board)
    row = int(input(f"Player {current_player}, enter row (0, 1, 2): "))
    col = int(input(f"Player {current_player}, enter column (0, 1, 2): "))

    if board[row][col] != " ":
      print("Cell already taken try again")
      continue

    board[row][col] = current_player  

    if check_winner(board, current_player):
      print_board(board)
      print(f"Player {current_player} wins!")
      break

    if is_full(board):
      print_board(board)
      print("It's a draw!")
      break
      
    else:
      print("Invalid move. Try again.")

    current_player = "O" if current_player == "X" else "X"


if  __name__ == "__main__":
  tik_tak_toe()