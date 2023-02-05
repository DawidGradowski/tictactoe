def set_board_size():
    while True:
        try:
            rows = int(input("Insert number of rows: "))
            cols = int(input("Insert number of columns: "))
            return (rows, cols)
        except:
            print("Invalid input! Try again: ")

def set_streak_to_win(rows, cols):
    while True:
        try:
            streak = int(input("Insert how many marks in row wins: "))
            if streak > rows or streak > cols or streak < 2:
                print("Invalid input! Try again: ")
            else:
                return streak
        except:
            print("Invalid input! Try again: ")

def create_board(rows, cols):
    board = []
    for y in range(rows):
        row = []
        for x in range(cols):
            row.append(" ")
        board.append(row)
    return board

rows, cols = set_board_size()
board = create_board(rows, cols)
streak = set_streak_to_win(rows, cols)

def main():
    global players
    global result
    result = " "
    number_of_players = set_number_of_players()
    players = create_players(number_of_players)
    turn = 0
    while True:
        draw_board()
        current_mark = get_current_mark(turn, number_of_players)
        x, y = input_move(current_mark)
        update_board(x, y, current_mark)
        turn += 1
        if is_game_resolved(turn):
            break

    draw_board()
    print(find_result())

def draw_board():
    for row in board:
        for tile in row:
            print(f"[{tile}]", end="")
        print()

def input_move(mark):
    while True:
        try:
            player = players[mark]
            print(f"{player}'s turn:")
            y = input("row?: ")
            x = input("column?: ")

            x = int(x)-1
            y = int(y)-1

            if is_move_correct(x, y):
                return (x, y)

        except:
            print("Invalid input, try again: ")

def is_move_correct(x,y):
    if x >= 0 and x <= cols-1 and y >= 0 and y <= rows-1:
        if board[y][x] == " ":
            return True
        else:
            print("Tile is occupied. Try again: ")
            return False
    else:
        print("Tile don't exist. Try again: ")

def get_current_mark(turn, number_of_players):
    global players
    current_player_id = turn % number_of_players
    marks = list(players.keys())
    return (marks[current_player_id])

def set_number_of_players():
    while True:
        try:
            number_of_players = int(input("Input number of players (min. 2): "))
            if number_of_players < 2:
                print("This value is too low! Try again: ")
            else:
                return number_of_players
        except:
            print("This is not a number! Try again: ")

def create_players(number_of_players):
    players = {}
    for i in range (0, number_of_players):
        player_created = False
        while player_created != True:
            mark = input(f"Player {i+1} mark: ")
            if mark in players.keys():
                print("This mark is already taken! Try again:")
            else:
                player = input(f"Player {i+1} name: ")
                if player in players.keys():
                    print("This name is already taken! Try again:")
                else:
                    players[mark] = player
                    player_created = True
    return players

def update_board(x, y, mark):
    board[y][x] = mark

def is_game_resolved(turn):
    global result
    check_columns()
    check_rows()
    check_crosses()

    if result != " ":
        return True
    elif turn == cols * rows:
        return True
    else:
        return False


def check_columns():
    global result
    for y in range (0, rows):
        for x in range (0, cols - streak + 1):
            if result == " " and column_win(x, y, streak):
                result = column_win(x, y, streak)

def column_win(x, y, streak):
    possible_winner = board[y][x]
    if possible_winner != " ":
        for i in range (streak):
            if possible_winner != board[y][x + i]:
                return False
        return possible_winner

    else:
        return False

def check_rows():
    global result
    for y in range (0, rows - streak + 1):
        for x in range (0, cols):
            if result == " " and row_win(x, y, streak):
                result = row_win(x, y, streak)

def row_win(x, y, streak):
    possible_winner = board[y][x]
    if possible_winner != " ":
        for i in range (streak):
            if possible_winner != board[y + i][x]:
                return False
        return possible_winner

    else:
        return False


def check_crosses():
    global result
    for y in range (0, rows - streak + 1):
        for x in range (0, cols - streak + 1):
            if result == " " and cross_win_one(x, y, streak):
                result = cross_win_one(x, y, streak)
    for y in range (streak - 1, rows):
        for x in range (0, cols - streak + 1):
            if result == " " and cross_win_two(x, y, streak):
                result = cross_win_two(x, y, streak)

def cross_win_one(x, y, streak):
    possible_winner = board[y][x]
    if possible_winner != " ":
        for i in range (streak):
            if possible_winner != board[y + i][x + i]:
                return False
        return possible_winner
    else:
        return False

def cross_win_two(x, y, streak):
    possible_winner = board[y][x]
    if possible_winner != " ":
        for i in range (streak):
            if possible_winner != board[y - i][x + i]:
                return False
        return possible_winner
    else:
        return False

def find_result():
    if result == " ":
        return "Draw!"
    else:
        winner = players[result]
        return f"{winner} wins!"


main()
