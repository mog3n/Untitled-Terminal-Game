from game.game_state import GameState
from game.game import play
import pickle

def new_game():
    print("NEW GAME")
    g = GameState(3, 3, 3)
    play(g)

def load_save():
    print("LOAD SAVE")
    try:
        save = open("save.p", "rb")
        g = pickle.load(save)
        save.close()
        play(g)
    except FileNotFoundError:
        print("NO SAVE FILE")

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
        print("QUITTING")
        return False

    else:
        print("NOT AN OPTION")

    return True
