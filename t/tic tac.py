import random
board = [' '] * 10
computer = 'X'
human = 'O'

def display(board):

    print(f'| {board[1]} | {board[2]} | {board[3]} |')
    print('-' * 13)
    print(f'| {board[4]} | {board[5]} | {board[6]} |')
    print('-' * 13)
    print(f'| {board[7]} | {board[8]} | {board[9]} |')


def check_win():
    if board[1] == board[2] == board[3] and board[1] != ' ':
        return True
    elif board[4] == board[5] == board[6] and board[4] != ' ':
        return True
    elif board[7] == board[8] == board[9] and board[7] != ' ':
        return True
    elif board[1] == board[4] == board[7] and board[1] != ' ':
        return True
    elif board[2] == board[5] == board[8] and board[2] != ' ':
        return True
    elif board[3] == board[6] == board[9] and board[3] != ' ':
        return True
    elif board[7] == board[5] == board[3] and board[7] != ' ':
        return True
    elif board[1] == board[5] == board[9] and board[1] != ' ':
        return True
    else:
        return False

def insert(letter,pos):
    if board[pos] == ' ':
        board[pos] = letter
        return True
    return False

def human_move(human):
    while True:
        pos = int(input('Enter a position (1-9): '))
        if pos < 1 or pos > 9:
            print("Invalid position! Try again.")
        elif insert(human, pos):
            break
        else:
            print("Position already taken! Try again.")

def computer_move(computer):
    while True:
        pos = random.randint(1, 9)
        if insert(computer, pos):
            break

while not check_win() and ' ' in board[1:]:
    display(board)
    human_move(human)
    if check_win():
        display(board)
        print("You win!")
        break
    if ' ' not in board[1:]:
        display(board)
        print("It's a draw!")
        break
    computer_move(computer)
    if check_win():
        display(board)
        print("Computer wins!")
        break