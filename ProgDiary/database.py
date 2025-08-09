import sqlite3
# This module handles the database operations for the ProgDiary application
connection = sqlite3.connect("data.db")

def create_table():
    with connection: # Create a table for diary entries if it doesn't exist
        connection.execute("CREATE TABLE entries (content TEXT, date TEXT);") # Create a table for diary entries if it doesn't exist

def add_entry(entry_content, entry_date):
    entries.append({"content": entry_content, "date": entry_date}) # Add entry to the list

def get_entries():
    return entries # Return the list of entries 
    
  

