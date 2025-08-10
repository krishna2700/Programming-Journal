from database import create_table, add_entry , get_entries

menu = """ Please select the following options:
1. Add a new entry for today
2. View entries
3. Exit

Your Selection: """
welcome = "Welcome to the Programming Diary!"

def prompt_new_entry(): 
     entry_content = input("What have you learned today? ") # Prompt user for entry content
     entry_date = input("Enter the date (YYYY-MM-DD): ") # Prompt user for entry date 
     add_entry(entry_content, entry_date) # Add a new entry to the diary database

def view_entries(entries):
    for entry in entries: # Loop through each entry in the list
        print(f"{entry['date']}\n{entry['content']}\n\n") # Print the date and content of each entry
     
print(welcome) # Print welcome message
create_table()
while (user_input := input(menu)) !="3": # Loop until user selects '3' to exit
    if user_input == "1":
        prompt_new_entry() # Prompt user to add a new entry
    elif user_input == "2":
        entries = get_entries() # View existing entries in the diary
        view_entries(entries) # Display the entries
    else:
        print("Invalid selection, please try again.")        

