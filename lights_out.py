def print_board(board):
    size = len(board)
    
    for i in range(size):
        print(f"\t{i + 1}", end="")
    print("\n")

    row_number = 1
    for row in board:
        lights = f"{row_number}\t"
        for light in row:

            if light:
                lights += "*\t"
            else:
                lights += "o\t"
        print(lights, "\n")
        row_number += 1

def game_over(board):
    for row in board:
        for light in row:
            if (light):
                return False

    return True

def toggle_light(board, row, column):
    size = len(board)
    
    board[row][column] = not board[row][column]

    if row - 1 >= 0:
        board[row - 1][column] = not board[row - 1][column]
    if row + 1 < size:
        board[row + 1][column] = not board[row + 1][column]
    if column - 1 >= 0:
        board[row][column - 1] = not board[row][column - 1]
    if column + 1 < size:
        board[row][column + 1] = not board[row][column + 1]

def acceptable_numbers(max):
    s = ""
    for i in range(max):
        s += str(i + 1)
        if i < max - 2:
            s += ", "
        elif i == max - 2:
            s += ", and "
    
    return s

def input_row_and_column(board_size):
    prompt = "Which light would you like to toggle (row column)? "

    while(True):
        input_str = input(prompt).strip().split(' ')
        row_and_column = list(map(lambda x : int(x) - 1, input_str))
        if len(row_and_column) < 2:
            print("Give both row and column number!")
            continue
        elif len(row_and_column) > 2:
            print("Just give a row and column number and nothing more!")
            continue
        else:
            row, column = row_and_column
            if row > board_size or column > board_size or row < 0 or column < 0:
                print("Row or column not in a valid range. Try again!")
                continue
            return row, column
board_size = 0

while(True):
    try:
        board_size = int(input("What board size do you like? 3x3 or 5x5?\nEnter either 3 or 5: "))
        if board_size == 3 or board_size == 5:
            break
    except:
        continue

board_row = [True for i in range(board_size)]
board = [board_row[:] for i in range(board_size)]

input("Enter the row and column number of the light you want to toggle separated with space (hit enter to continue).")
input(f"Enter a random character other than {acceptable_numbers(board_size)} to accept defeat (hit enter to start).")

while(not game_over(board)):
    print_board(board)

    try:
        row, column = input_row_and_column(board_size)
    except:
        print("Bye loser!")
        break
    toggle_light(board, row, column)
else:
    print("\n")
    print("*******************************")
    print("H U R R A Y !   Y O U   W O N !")
    print("*******************************")
