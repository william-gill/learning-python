def print_board():
    print (" {} | {} | {}".format(game_state[1],game_state[2],game_state[3]))
    print ("-----------")
    print (" {} | {} | {}".format(game_state[4],game_state[5],game_state[6]))
    print ("-----------")
    print (" {} | {} | {}".format(game_state[7],game_state[8],game_state[9]))


game_state = [' ','X','X',' ',' ',' ',' ',' ',' ',' ']
print_board()
