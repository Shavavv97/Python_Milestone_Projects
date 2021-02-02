board = {'7': ' ' , '8': ' ' , '9': ' ' ,
        '4': ' ' , '5': ' ' , '6': ' ' ,
        '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in board:
    board_keys.append(key)

def matrix(board):
    print('|' + board['7'] + '|' + board['8'] + '|' + board['9'] + '|')
    print('|' + board['4'] + '|' + board['5'] + '|' + board['6'] + '|')
    print('|' + board['1'] + '|' + board['2'] + '|' + board['3'] + '|\n')

def game():

    choices = ('O', 'X')

    player_1 = input('Player 1, choose between X or O:\n').upper()

    while (player_1 not in choices):
        print('Sorry, that is not a choice, please choose between X or O')
        player_1 = input('Player 1, choose between X or O:\n').upper()

    if (player_1 == 'X'):
        choice = 'X'
    elif (player_1 == 'O'):
        choice = 'O'

    count = 0

    for i in range(10):
        matrix(board)

        move = input("It's choice of " + choice + "'s. Choose a place with your numeric keyboard: ")

        while move not in board_keys:
            move = input("Sorry, that is not a choice. It's choice of " + choice + "'s. Choose a place with your numeric keyboard: ")

        if board[move] == ' ':
            board[move] = choice
            count += 1
        else:
            print("That place is taken.\nChoose another place: ")
            continue

        if count >= 5:
            if board['7'] == board['8'] == board['9'] != ' ':
                matrix(board)
                print("Game Over.\n")                
                print(choice + "'s won.")                
                break
            elif board['4'] == board['5'] == board['6'] != ' ':
                matrix(board)
                print("Game Over.\n")                
                print(choice + "'s won.")
                break
            elif board['1'] == board['2'] == board['3'] != ' ':
                matrix(board)
                print("Game Over.\n")                
                print(choice + "'s won.")
                break
            elif board['1'] == board['4'] == board['7'] != ' ':
                matrix(board)
                print("Game Over.\n")                
                print(choice + "'s won.")
                break
            elif board['2'] == board['5'] == board['8'] != ' ':
                matrix(board)
                print("Game Over.\n")                
                print(choice + "'s won.")
                break
            elif board['3'] == board['6'] == board['9'] != ' ':
                matrix(board)
                print("Game Over.\n")                
                print(choice + "'s won.")
                break 
            elif board['7'] == board['5'] == board['3'] != ' ':
                matrix(board)
                print("Game Over.\n")                
                print(choice + "'s won.")
                break
            elif board['1'] == board['5'] == board['9'] != ' ':
                matrix(board)
                print("Game Over.\n")                
                print(choice + "'s won.")
                break 

        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        if choice =='X':
            choice = 'O'
        else:
            choice = 'X'

    restart = input("Do want to play Again? (y/n) ").upper()

    while restart not in ('Y', 'N'):
        restart = input("That is not an option. Do want to play Again? (y/n) ").upper()

    if restart == "Y":  
        for key in board_keys:
            board[key] = " "

        game()

if __name__ == "__main__":
    game()