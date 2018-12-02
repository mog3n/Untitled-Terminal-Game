from utils.game_input import game_input

def play(g):
    while(g.isRunning()):
        print(g)
        user_in = input('Enter: ')
        game_input(user_in, g)
