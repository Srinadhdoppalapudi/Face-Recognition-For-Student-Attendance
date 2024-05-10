import sqlite3

# Connect to the database
conn = sqlite3.connect('dbfile.db')

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Delete records with a specific condition
# Example: Delete the record for roll number '15'
roll_to_delete = '10'
cursor.execute("DELETE FROM studentdb WHERE roll = ?", (roll_to_delete,))

# Commit the changes to the database
conn.commit()

print("Record(s) deleted successfully!")

# Close the connection
conn.close()
