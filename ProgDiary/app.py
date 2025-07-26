menu = """ Please select the following options:
1. Add a new entry for today
2. View entries
3. Exit

Your Selection: """
welcome = "Welcome to the Programming Diary!"

while (user_input := input(menu)) !="3": # Loop until user selects '3' to exit
    if user_input == "1":
        print("Adding...")
    elif user_input == "2":
        print("Viewing...")
    else:
        print("Invalid selection, please try again.")        

