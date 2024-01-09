import pyodbc

# Connection string
# Replace 'YourDatabase.accdb' with the actual name of your Access database file
# Replace 'C:\\path\\to\\your\\database\\' with the actual path to your Access database file
connection_string = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Abdullah\OneDrive\Desktop\ACCESS\FOOD_INSERT.accdb;'

# Establish a connection
connection = pyodbc.connect(connection_string)

# Create a cursor
cursor = connection.cursor()

# Example query
query = "SELECT * FROM FOOD_DATA"
print(f"Executing query: {query}")

# Execute the query
cursor.execute(query)

# Fetch and print only the first row
row = cursor.fetchone()
if row:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()
