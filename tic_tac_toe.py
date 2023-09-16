def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    game_over = False

    while not game_over:
        print_board(board)
        row, col = -1, -1

        while True:
            try:
                row = int(input(f"Player {current_player}, enter row (1-3): ")) - 1
                col = int(input(f"Player {current_player}, enter column (1-3): ")) - 1

                if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                    break
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Enter a number between 1 and 3.")

        board[row][col] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            game_over = True
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            game_over = True
        else:
            current_player = "O" if current_player == "X" else "X"

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        main()
    else:
        print("Thanks for playing!")

if __name__ == "__main__":
    main()
