from utils.menu_input import menu_input

def menu_display():
    menu = open('texts/menu.txt', 'r')
    content = menu.read()
    menu.close()
    print(content)

def main():
    menu_display()

    user_in = None
    while(user_in != 'q'):
        user_in = input('Enter: ')
        menu_input(user_in)

if(__name__ == '__main__'):
    main()
