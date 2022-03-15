# Game number: 0 
# game name: SOS game 
# done by: Basmala Mohamed Sayed Gad 
# Id: 20210090
board = [
    [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    , [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    , [' ', ' ', ' 1', ' 2', ' 3', ' 4', ' ', ' ']
    , [' ', ' ', ' 5', ' 6', ' 7', ' 8', ' ', ' ']
    , [' ', ' ', ' 9', '10', '11', '12', ' ', ' ']
    , [' ', ' ', '13', '14', '15', '16', ' ', ' ']
    , [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    , [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
]
valid_boxes = 16
box = 0
row = 0
col = 0
score = 0
letter = " "
player_1_score = 0
player_2_score = 0
winner = False
l = []

def display_board():
    global player_1_score, player_2_score
    print()
    print("PLAYER 1: ", player_1_score, "  ", "PLAYER 2: ", player_2_score)
    for row in board:
        print(*row[2:6], sep=" ")  # to print only the rows which have numbers 


def player_1():
    global box, letter

    box = input("\nPLAYER 1, Please enter box number:")
    while box.isdigit() not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]:
        box = input("Invalid number, Please enter anthor number:")
    box = int(box)
    while box < 1 or box > 16:
        box = int(input("Invalid number, Please enter anthor number:"))
    letter = input("\nPLAYER 1, PLease enter letter (S or O) :")
    letter = letter.upper()
    while (letter != "S") and (letter != "O"):
        letter = input("\nInvalid letter, try again :")
        letter = letter.upper()
    row_and_column()

def player_2():
    global box, letter

    box = input("\nPLAYER 2, Please enter box number:")
    while box.isdigit() not in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]:
        box = input("Invalid number, Please enter anthor number:")
    box = int(box)
    while box < 1 or box > 16:
        box = int(input("Invalid number, Please enter anthor number:"))
    letter = input("\nPLAYER 2, PLease enter letter (S or O) :")
    letter = letter.upper()
    while (letter != "S") and (letter != "O"):
        letter = input("\nInvalid letter, try again :")
        letter = letter.upper()
    row_and_column()


def row_and_column():
    global valid_boxes
    global row
    global col

    if box == 1:
        row = 2
        col = 2
    elif box == 2:
        row = 2
        col = 3
    elif box == 3:
        row = 2
        col = 4
    elif box == 4:
        row = 2
        col = 5
    elif box == 5:
        row = 3
        col = 2
    elif box == 6:
        row = 3
        col = 3
    elif box == 7:
        row = 3
        col = 4
    elif box == 8:
        row = 3
        col = 5
    elif box == 9:
        row = 4
        col = 2
    elif box == 10:
        row = 4
        col = 3
    elif box == 11:
        row = 4
        col = 4
    elif box == 12:
        row = 4
        col = 5
    elif box == 13:
        row = 5
        col = 2
    elif box == 14:
        row = 5
        col = 3
    elif box == 15:
        row = 5
        col = 4
    elif box == 16:
        row = 5
        col = 5

    board[row][col] = letter  # to replace board elemrnt with letter (2D list)
    valid_boxes -= 1
    return row, col


def check_winner():
    global winner, score 
    score = 0 
    winner = False
    # 3 conditions same row and different columns
    if board[row][col] + board[row][col + 1] + board[row][col + 2] == "SOS" :  # case num 1 if input is "S"
        temp = [[row, col], [row, col+1], [row, col+2]]
        if temp not in l:
            winner = True
            score += 1
            l.append(temp)
    if board[row][col - 2] + board[row][col - 1] + board[row][col] == "SOS" :  # case num 2 if input is "S"
        temp = [[row, col-2], [row, col-1], [row, col]]
        if temp not in l:
            winner = True
            score += 1
            l.append(temp)
    if board[row][col - 1] + board[row][col] + board[row][col + 1] == "SOS" :  # case num 3 if input is "O"
        temp = [[row, col-1], [row, col], [row, col+1]]
        if temp not in l:
            winner = True
            score += 1
            l.append(temp)


    # 3 conditions same column and different rows
    if board[row][col] + board[row + 1][col] + board[row + 2][col] == "SOS" :  # case num 1 if input is "S"
        temp = [[row, col], [row+1, col], [row+2, col]]
        if temp not in l:
            winner = True
            score += 1
            l.append(temp)
    if board[row][col] + board[row - 1][col] + board[row - 2][col] == "SOS" :  # case num 2 if input is "S"
        temp = [[row, col], [row-1, col], [row-2, col]]
        if temp not in l:
            winner = True
            score += 1
            l.append(temp)
    if board[row - 1][col] + board[row][col] + board[row + 1][col] == "SOS" :  # case num 3 if input is "O"
        temp = [[row-1, col], [row, col], [row+1, col]]
        if temp not in l:
            winner = True
            score += 1
            l.append(temp)


    # 6 cross conditions
    if board[row][col] + board[row - 1][col + 1] + board[row - 2][
        col + 2] == "SOS" :  # case num 1 if input is "S" (UP + R)
        temp = [[row, col], [row-1, col+1], [row-2, col+2]]
        if temp not in l:
            winner = True
            score += 1
            l.append(temp)
    if board[row][col] + board[row + 1][col + 1] + board[row + 2][
        col + 2] == "SOS" :  # case num 2 if input is "S" (DOWN + R)
        temp = [[row, col], [row+1, col+1], [row+2, col+2]]
        if temp not in l:
            winner = True
            score += 1
            l.append(temp)
    if board[row][col] + board[row - 1][col - 1] + board[row - 2][
        col - 2] == "SOS":  # case num 3 if input is "S" (UP + L)
        temp = [[row, col], [row-1, col-1], [row-2, col-2]]
        if temp not in l:
            winner = True
            score += 1
            l.append(temp)
    if board[row][col] + board[row + 1][col - 1] + board[row + 2][
        col - 2] == "SOS" :  # csae num 4 if input is "S" (DOWN + L)
        temp = [[row, col], [row+1, col-1], [row+2, col-2]]
        if temp not in l:
            winner = True
            score += 1
            l.append(temp)
    if board[row + 1][col - 1] + board[row][col] + board[row - 1][
        col + 1] == "SOS" :  # case num 5 if input is "O" (R)
        temp = [[row+1, col-1], [row, col], [row-1, col+1]]
        if temp not in l:
            winner = True
            score += 1
            l.append(temp)
    if board[row - 1][col - 1] + board[row][col] + board[row + 1][
        col + 1] == "SOS" :  # case num 6 if input is "O" (L)
        temp = [[row-1, col-1], [row, col], [row+1, col+1]]
        if temp not in l:
            winner = True
            score += 1
            l.append(temp)

    if winner == False:
        print("\nOOPS :( TRY AGAIN..")
    return winner, score


def Game():
    global player_1_score, player_2_score, score, row, col

    while (True):

        display_board()
        player_1()
        check_winner()
        if winner == True:
            player_1_score += score

        while (winner == True):
            if valid_boxes == 0:
                break
            print("\nPLAYER 1 WINS :) KEEP PLAYING..")
            display_board()
            player_1()
            check_winner()
            if winner == True:
                player_1_score += score
        if valid_boxes == 0:
            print("\nGAME OVER !")
            break
        display_board()
        player_2()
        check_winner()
        if winner == True:
            player_2_score += score

        while (winner == True):
            if valid_boxes == 0:
                break
            print("\nPLAYER 2 WINS :) KEEP PLAYING..")
            display_board()
            player_2()
            check_winner()
            if winner == True:
                player_2_score += score

        if valid_boxes == 0:
            print("\nGAME OVER !")
            break
    if player_1_score > player_2_score:
        print("\nPLAYER 1 IS WINNER :) !!!","PLAYER 1 SCORE = ", player_1_score ," PLAYER 2 SCORE = ",player_2_score)
    elif player_2_score > player_1_score:
        print("\nPLAYER 2 IS WINNER :) !!!","PLAYER 1 SCORE = ", player_1_score ," PLAYER 2 SCORE = ",player_2_score)
    elif player_2_score == player_1_score != 0:
        print("DRAW")

Game()