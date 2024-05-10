import sqlite3

# Open a connection to the database
conn = sqlite3.connect('dbfile.db')

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# Execute a query to get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch and print all table names
tables = cursor.fetchall()
print("Tables:", tables)

# Assuming you've already established a connection
cursor.execute("PRAGMA table_info(studentdb);")

# Fetch and display the table structure
table_info = cursor.fetchall()
print("Table Structure:")
for column in table_info:
    print(column)

# Retrieve all data from the 'studentdb' table
cursor.execute("SELECT * FROM studentdb;")

# Fetch and display the first few rows
rows = cursor.fetchmany(10)  # Adjust the number to fetch more or fewer rows
print("Table Data:")
for row in rows:
    print(row)

conn.close()