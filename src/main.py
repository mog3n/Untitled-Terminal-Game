def menu():
    menu = open('texts/menu.txt', 'r')
    content = menu.read()
    menu.close()
    print(content)

def main():
    menu()
    user_in = None
    while(user_in != 'q'):
        user_in = input('Enter: ')

if(__name__ == '__main__'):
    main()
