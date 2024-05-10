import sqlite3

# Open a connection to the database
conn = sqlite3.connect('dbfile.db')

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Insert a new record into 'studentdb'
new_record = (
    '48',  # Roll number
    'Ameen',  # Name
    'CSE',  # Branch
    '2021-05-01',  # Date
    '08:30:00',  # Time
    'present'  # Status
)

# Insert the record into 'studentdb'
cursor.execute("INSERT INTO studentdb (roll, name, branch, mdate, mtime, status) VALUES (?, ?, ?, ?, ?, ?)", new_record)

# Commit the changes to the database
conn.commit()

print("New record added successfully!")

# Retrieve all data from the 'studentdb' table
cursor.execute("SELECT * FROM studentdb;")

# Fetch and display the first few rows
rows = cursor.fetchmany(10)  # Adjust the number to fetch more or fewer rows
print("Table Data:")
for row in rows:
    print(row)


# Close the connection when done
conn.close()
