def print_board(board):
    print("\t1\t2\t3\n")
    r = 1
    for row in board:
        lights = f"{r}\t"
        for light in row:

            if light:
                lights += "*\t"
            else:
                lights += "o\t"
        print(lights, "\n")
        r += 1

def game_over(board):
    for row in board:
        for light in row:
            if (light):
                return False

    return True

def toggle_light(board, row, column):
    board[row][column] = not board[row][column]

    if row - 1 >= 0:
        board[row - 1][column] = not board[row - 1][column]
    if row + 1 < 3:
        board[row + 1][column] = not board[row + 1][column]
    if column - 1 >= 0:
        board[row][column - 1] = not board[row][column - 1]
    if column + 1 < 3:
        board[row][column + 1] = not board[row][column + 1]

    return board

board = [[True, True, True], [True, True, True], [True, True, True]]
prompt = "Which light would you like to toggle (row column)? "

print("(enter a random character other than 1, 2, and 3 to accept defeat.)\n\n")

while(not game_over(board)):
    print_board(board)
    try:
        input_str = input(prompt).split(' ')
        row, column = map(lambda x : int(x) - 1, input_str)
    except:
        print("loser...")
        break
    board = toggle_light(board, row, column)
else:
    print("\n")
    print("*******************************")
    print("H U R R A Y !   Y O U   W O N !")
    print("*******************************")
