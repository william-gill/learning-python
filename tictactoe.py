def print_board():
    print (" {} | {} | {}".format(game_state[1],game_state[2],game_state[3]))
    print ("-----------")
    print (" {} | {} | {}".format(game_state[4],game_state[5],game_state[6]))
    print ("-----------")
    print (" {} | {} | {}".format(game_state[7],game_state[8],game_state[9]))

def check_move(move):
    if 0 <= move < 10:
        if game_state[move] == ' ':
            return True
        else:
            return False
    else:
        return False

def check_win():
    if game_state[1] == 'X' and game_state[2] == 'X' and game_state[3] == 'X': return True
    if game_state[4] == 'X' and game_state[5] == 'X' and game_state[6] == 'X': return True
    if game_state[7] == 'X' and game_state[8] == 'X' and game_state[9] == 'X': return True
    if game_state[1] == 'X' and game_state[4] == 'X' and game_state[7] == 'X': return True
    if game_state[2] == 'X' and game_state[5] == 'X' and game_state[8] == 'X': return True
    if game_state[3] == 'X' and game_state[6] == 'X' and game_state[9] == 'X': return True
    if game_state[1] == 'X' and game_state[5] == 'X' and game_state[9] == 'X': return True
    if game_state[3] == 'X' and game_state[5] == 'X' and game_state[7] == 'X': return True
    if game_state[1] == 'O' and game_state[2] == 'O' and game_state[3] == 'O': return True
    if game_state[4] == 'O' and game_state[5] == 'O' and game_state[6] == 'O': return True
    if game_state[7] == 'O' and game_state[8] == 'O' and game_state[9] == 'O': return True
    if game_state[1] == 'O' and game_state[4] == 'O' and game_state[7] == 'O': return True
    if game_state[2] == 'O' and game_state[5] == 'O' and game_state[8] == 'O': return True
    if game_state[3] == 'O' and game_state[6] == 'O' and game_state[9] == 'O': return True
    if game_state[1] == 'O' and game_state[5] == 'O' and game_state[9] == 'O': return True
    if game_state[3] == 'O' and game_state[5] == 'O' and game_state[7] == 'O': return True


turns = 0
player_turn = 1
game_state = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

while turns < 9:
    print (check_win())
    player_input = int(input('Player {}: '.format(player_turn)))
    if check_move(player_input) == True:
        if player_turn == 1: game_state[player_input] = 'X'
        else: game_state[player_input] = 'O'
        if player_input == 0:
            break
        print_board()
        if check_win() == True:
            print ('Congratulations Player {}!'.format(player_turn))
            break
        if player_turn == 1: player_turn = 2
        else: player_turn = 1
        turns += 1
    else:
        print ("Move not allowed. Try again.")

if check_win() != True:
    print ('No more moves - no winner this time!')
