from game.game_state import GameState

def new_game():
    print("NEW GAME")
    g = GameState()
    print(g)

def load_save():
    print("LOAD SAVE")

def help():
    help = open('texts/help.txt', 'r')
    content = help.read()
    help.close()
    print(content)

def menu_input(i):
    if(i == 'n'):
        new_game()

    elif(i == 'l'):
        load_save()

    elif(i == 'h'):
        help()

    elif(i == 'q'):
        pass

    else:
        print("NOT AN OPTION")
