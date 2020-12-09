#Define board for the game
game_board = {
    'A1': ' ','A2':' ','A3':' ',
    'B1': ' ','B2':' ','B3':' ',
    'C1': ' ','C2':' ','C3':' '
}

# Define variables
player = 1
moves = 0

# Print the board for the players
print('********')
print('A1|A2|A3')
print('--+--+--')
print('B1|B2|B3')
print('--+--+--')
print('C1|C2|C3')
print('********')

# Define the board as a function to be call each iteration
def gui():
    print(game_board['A1'] + '|'+ game_board['A2'] +  '|'+ game_board['A3'])
    print('-+-+-')
    print(game_board['B1'] + '|'+ game_board['B2'] +  '|'+ game_board['B3'])
    print('-+-+-')
    print(game_board['C1'] + '|'+ game_board['C2'] +  '|'+ game_board['C3'])

def validate():
    #-----------------------------HORIZONTAL-PLAYER-ONE------------------------------------------
    if game_board['A1'] == 'X' and game_board['A2'] == 'X' and game_board['A3'] == 'X':
        print("Player one Won!!!")
        return 1
    if game_board['B1'] == 'X' and game_board['B2'] == 'X' and game_board['B3'] == 'X':
        print("Player one Won!!!")
        return 1
    if game_board['C1'] == 'X' and game_board['C2'] == 'X' and game_board['C3'] == 'X':
        print("Player one Won!!!")
        return 1   
    #-----------------------------VERTICAL-PLAYER-ONE-------------------------------------------
    if game_board['A1'] == 'X' and game_board['B1'] == 'X' and game_board['C1'] == 'X':
        print("Player one Won!!!")
        return 1
    if game_board['A2'] == 'X' and game_board['B2'] == 'X' and game_board['C2'] == 'X':
        print("Player one Won!!!")
        return 1
    if game_board['A3'] == 'X' and game_board['B3'] == 'X' and game_board['C3'] == 'X':
        print("Player one Won!!!")
        return 1 
    #-----------------------------DIAGONAL-PLAYER-ONE-------------------------------------------
    if game_board['A1'] == 'X' and game_board['B2'] == 'X' and game_board['C3'] == 'X':
        print("Player one Won!!!")
        return 1
    if game_board['A3'] == 'X' and game_board['B2'] == 'X' and game_board['C1'] == 'X':
        print("Player one Won!!!")
        return 1 
    #-----------------------------HORIZONTAL-PLAYER-TWO-------------------------------------------
    if game_board['A1'] == 'O' and game_board['A2'] == 'O' and game_board['A3'] == 'O':
        print("Player two Won!!!")
        return 1
    if game_board['B1'] == 'O' and game_board['B2'] == 'O' and game_board['B3'] == 'O':
        print("Player two Won!!!")
        return 1
    if game_board['C1'] == 'O' and game_board['C2'] == 'O' and game_board['C3'] == 'O':
        print("Player two Won!!!")
        return 1   
    #-----------------------------VERTICAL-PLAYER-TWO-------------------------------------------
    if game_board['A1'] == 'O' and game_board['B1'] == 'O' and game_board['C1'] == 'O':
        print("Player two Won!!!")
        return 1
    if game_board['A2'] == 'O' and game_board['B2'] == 'O' and game_board['C2'] == 'O':
        print("Player two Won!!!")
        return 1
    if game_board['A3'] == 'O' and game_board['B3'] == 'O' and game_board['C3'] == 'O':
        print("Player two Won!!!")
        return 1 
    #-----------------------------DIAGONAL-PLAYER-TWO-------------------------------------------
    if game_board['A1'] == 'O' and game_board['B2'] == 'O' and game_board['C3'] == 'O':
        print("Player two Won!!!")
        return 1
    if game_board['A3'] == 'O' and game_board['B2'] == 'O' and game_board['C1'] == 'O':
        print("Player two Won!!!")
        return 1 
    return 0
    
while True:
    gui()
    if moves == 9 or validate() == 1:
        break
    while True:
        if player == 1:
            user_one = input("Player One: ")
            if user_one.upper() in game_board and game_board[user_one.upper()] == ' ':
                game_board[user_one.upper()]='X'
                player = 2
                break
            else:
                print('No valid option')
                continue
        else:
            user_two = input("Player Two: ")
            if user_two.upper() in game_board and game_board[user_two.upper()] == ' ':
                game_board[user_two.upper()]='O'
                player = 1
                break
            else:
                print('No valid option')
                continue
    moves += 1
    

