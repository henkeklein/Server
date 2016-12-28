import io
import os
firstname = ''
lastname = ''
country = ''
path = 'players.txt'
def add_player(firstname, lastname, country):
    f = open('players.txt', 'a')
    firstname = raw_input("Firstname: \n")
    lastname = raw_input("Lastname: \n")
    country = raw_input("Country: \n")
    f.write(firstname+ ',' + lastname+ ',' + country + '\n')
    f.close()

def print_players():
    f = open('players.txt', 'r')
    file_contents = f.read()
    print (file_contents)
    f.close()

def check_file():
    if(os.path.isfile(path)):
        print 'File exist'
    else:
        with io.FileIO("players.txt", "w") as file:
            file.write('')
            print 'New file created'

def start():
    check_file()
    while True:
            choice = raw_input("Choose: (1) Add player, (2) List all players\n")
            if choice == '1':
                add_player(firstname, lastname, country)
            elif choice == "2":
                print_players()
            else:
                print 'Bye!'
                break



start()
