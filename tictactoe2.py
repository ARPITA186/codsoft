import math
tictactoeboard = [' ' for _ in range(9)]
def print_tictactoeboard():

        for i in range(0,9,3):
            print(tictactoeboard[i] + '|' + tictactoeboard[i+1] + '|' + tictactoeboard[i+2])
            if i<6:
               print('-+--+-')
def is_winner(gplayer):
        win_type=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
        return any(all(tictactoeboard[i]==gplayer for i in a)for a in win_type)
def is_draw():
        return ' 'not in tictactoeboard and not is_winner('X') and not is_winner('O')
def minimax(is_maximize):
    if is_winner('O'):
        return 1
    if is_winner('X'):
        return -1
    if is_draw():
        return 0
    if is_maximize:
        best_score = -math.inf
        for i in range(9):
            if tictactoeboard[i] == ' ':
                tictactoeboard[i] = 'O'
                score = minimax(False)
                tictactoeboard[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score=math.inf
        for i in range(9):
         if tictactoeboard[i]==' ':
                tictactoeboard[i]='X'
                score=minimax(True)
                tictactoeboard[i]=' '
                best_score=min(score,best_score)
        return best_score
def best_move():
        best_score=-math.inf
        best_move=-1
        for i in range(9):
            if tictactoeboard[i]==' ':
                tictactoeboard[i]='O'
                score=minimax(False)
                tictactoeboard[i]=' '
                if score>best_score:
                    best_score=score
                    best_move=i

            if best_move == -1:
             for i in range(9):
              if tictactoeboard[i] == ' ':
                return i
        return best_move
def startplay():
    print("Welcome to our Tic-Tac-Toe! You are the 'X', AI is the 'O'.")
    print_tictactoeboard()


    while True:
        try:
            move = int(input("Enter your move (0-8): "))
            if move < 0 or move > 8 or tictactoeboard[move] != ' ':
                print("Invalid move! Try again.")
                continue
        except ValueError:
            print("...Ahh! Invalid input! Please enter a number between 0 and 8...")
            continue

        tictactoeboard[move] = 'X'
        print_tictactoeboard()

        if is_winner('X'):
                print(".....Congrats!You won! Hurray!.....")
                break
        if is_draw():
                print(".....It's Draw!......")
                break
        agent_move=best_move()
        tictactoeboard[agent_move]='O'
        print("Agent's move")
        print_tictactoeboard()

        if is_winner('O'):
            print("......Agent is winner! Better luck next time!.....")
            break
        if is_draw():
            print("It's a draw")
            break
startplay()