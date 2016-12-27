import json
from pprint import pprint

def add_player(player):
    f = open('players.json')
    data = json.load(f)
    data["players"].append(player)
    f.close()

    writing_file = open('players.json', 'w')
    writing_file.write(json.dumps(data, sort_keys=True, indent=4, separators=(',',': ')))
    writing_file.close()

def print_players():
    f = open('players.json', 'r')
    file_contents = json.load(f)
    pprint(file_contents)
    f.close()

def start():
    while True:
        choice = raw_input("Choose: (1) Add player, (2) List all players\n")
        if choice == '1':
                firstname = raw_input("Firstname: \n")
                lastname = raw_input("Lastname: \n")
                country = raw_input("Country: \n")
                data_dict = {
                    "firstname":firstname,
                    "lastname":lastname,
                    "country":country
                }
                add_player(data_dict)
        elif choice == "2":
            print_players()
        else:
            print 'Bye!'
            break

start()
