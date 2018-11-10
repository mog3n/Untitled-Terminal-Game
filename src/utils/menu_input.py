def new_game():
    print("NEW GAME")

def load_save():
    print("LOAD SAVE")

def help():
    print("HELP")

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
