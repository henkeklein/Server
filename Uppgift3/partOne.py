# Start a infinite loop
my_dict = []
while True:
    choice = raw_input("Choose: (1) Add person, (2) List all\n")
    # Store user choice in a variable
    if choice == '1':
            name = raw_input('Enter your full name: ')
            my_dict.append(name)
    elif choice == "2":
        # Go through the list and print everyone
        for person in my_dict:
            print (person)
    else:
        print 'Bye!'
        break
