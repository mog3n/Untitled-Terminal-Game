from game.game_state import GameState
import pickle

def game_input(i, g):
    if(i == 's'):
        print("SAVING")
        save = open("save.p", "wb+")
        pickle.dump(g, save)
        save.close()

    elif(i == 'q'):
        print("QUITTING, BACK TO MAIN MENU")
        g.stop()

    elif(i == 'y'):
        print("ROUND PASSED")
        g.round()

    else:
        print("NOT AN OPTION")
