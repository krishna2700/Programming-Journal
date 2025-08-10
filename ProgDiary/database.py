import sqlite3
# This module handles the database operations for the ProgDiary application
connection = sqlite3.connect("data.db")
connection.row_factory = sqlite3.Row # Set row factory to return rows as dictionaries

def create_table():
    with connection: # Create a table for diary entries if it doesn't exist
        connection.execute("CREATE TABLE IF NOT EXISTS entries (content TEXT, date TEXT);") # Create a table for diary entries if it doesn't exist

def add_entry(entry_content, entry_date):
    with connection: # Add a new entry to the diary database
        connection.execute("INSERT INTO entries VALUES (?,?);", (entry_content, entry_date)) # Add a new entry to the diary database
def get_entries():
    with connection: # Retrieve all entries from the diary database
        cursor = connection.cursor() # Retrieve all entries from the diary database
        cursor.execute("SELECT * FROM entries ORDER BY date DESC;") # Retrieve all entries from the diary database
        entries = cursor.fetchall() # Retrieve all entries from the diary database
        return entries
    


