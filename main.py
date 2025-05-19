import random

board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
players = [0, 'O', 'X']
available_moves = [str(num) for num in range(0, 10)]

def display_board(a, b):
    print("Варианты\nходов Доска" + "\n\n" +
    a[7] + '|' + a[8] + '|' + a[9] + ' ' + b[7] + '|' + b[8] + '|' +
    board[9] + " \n" +
    '----- -----' + "\n" +
    a[4] + '|' + a[5] + '|' + a[6] + ' ' + b[4] + '|' + b[5] + '|' +
    board[6] + " \n" +
    '----- -----' + "\n" +
    a[1] + '|' + a[2] + '|' + a[3] + ' ' + b[1] + '|' + b[2] + '|' +
    board[3])

def play_display(a, b):
    print('\n'*100)
    print(a[7] + '|' + a[8] + '|' + a[9] + ' ' + b[7] + '|' + b[8] + '|' +
    b[9] + " \n" +
    '----- -----' + "\n" +
    a[4] + '|' + a[5] + '|' + a[6] + ' ' + b[4] + '|' + b[5] + '|' +
    board[6] + " \n" +
    '----- -----' + "\n" +
    a[1] + '|' + a[2] + '|' + a[3] + ' ' + b[1] + '|' + b[2] + '|' +
    board[3])

def rule():
    print("Привет, пора поиграть в крестики-нолики!")
    print("Правила просты, победит тот кто соберет в ряд или по диаганали 3 крестика или нолика")
    print("Надеюсь ты нашел себе соперника")
    print("Что же, давай начнем!")

def win_cheak(board, marker):
    return ((board[7] == board[8] == board[9] == marker) or
    (board[4] == board[5] == board[6] == marker) or
    (board[1] == board[2] == board[3] == marker) or
    (board[7] == board[4] == board[1] == marker) or
    (board[8] == board[5] == board[2] == marker) or
    (board[9] == board[6] == board[3] == marker) or
    (board[7] == board[5] == board[3] == marker) or
    (board[9] == board[5] == board[1] == marker))

def place_markers(board, position, marker, available_moves):
    board[position] = marker
    available_moves[position] = ' '

def choice_checker(board, position):
    return board[position] == " "

def random_player():
    return random.choice((-1, 1))

def player_choice(player):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not choice_checker(board, position):
        position = int(input(f'Игрок {player} выберите следующую клетку: (1-9) '))

    return position

def full_board_check(board):
    return " " not in board

def replay():
    print("Хотели бы вы поиграть еще?")
    qest = input("Yes or No? ").lower()[0]
    return qest == "y"

rule()
display_board(available_moves, board)

while True:
    triger = random_player()
    player = players[triger]
    print(f'Игрок {player} ходит первым')

    game_on = True
    input("Нажмите Enter")
    while game_on:
        play_display(available_moves, board)
        position = player_choice(player)
        place_markers(board, position, player, available_moves)

        if win_cheak(board, player):
            play_display(available_moves, board)
            print(f'В этой битве победил игрок {player}!')
            game_on = False
        else:
            if full_board_check(board):
                play_display(available_moves ,board)
                print("Ничья")
                game_on = False
            else:
                triger *= -1
                player = players[triger]
                print('\n'*100)

    available_moves = [str(num) for num in range(0, 10)]
    board = [' '] * 10
    if not replay():
        break
