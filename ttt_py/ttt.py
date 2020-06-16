from players import Players, read_scoreboard, display_scoreboard

def main():

    p1, p2 = introduction()

    p1 = Players(p1, "X")
    p2 = Players(p2, "O")

    check_for_name(p1, p2)

    ready = ready_check()

    rules()

    p1.turn()
    p2.turn()



    

def introduction():
    
    print("======================\nWelcome to tic-tac-toe\n======================")
    
    p1 = input("\nPlease enter player's 1 name:\n")
    p2 = input("\nPlease enter player's 2 name:\n")

    return p1, p2


def ready_check():
    
    ready = input("\nAre you ready to start the game?:    (y/n)\n")
    
    if ready != 'y':
        print("\nWhen you are ready just type in 'y'\n")
        return ready_check()
    
    else:
        return ready

def check_for_name(p1, p2):
    
    dic = read_scoreboard()

    if not p1.name in dic.keys():
        p1.first_init()
    
    elif not p2.name in dic.keys():
        p2.first_init()
    
    else:
        pass

def rules():
    
    y_or_n = input("\nDo you want to read the rules?   (y/n)\n")
    
    if y_or_n != 'y' and y_or_n != 'n':
        print("\nPlease enter 'y' or 'n'\n")
        return rules()
    
    elif y_or_n == 'n':
        return
    
    else:
        print(
            """\n\nIn the 3x3 grid both players will take turn to place their mark (player 1 with 'X' and player 2 with 'O')\n
The goal is getting three marks in a horizontal, vertical, or diagonal row\n
The player who get it first is the winner.\n
If there is no more rooam on the grid for any mark and none of the players got 3 stright then its a tie.\n
In an event of a tie both players will get a loss."""
            )


main()
