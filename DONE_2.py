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

# Use a dictionary to store processed values for each identifier
processed_values = {}

# Specify the identifier you want to filter for
filter_identifier = 20

# Execute the query
cursor.execute(query)

# Fetch and print the results for the specified identifier
for row in cursor.fetchall():
    if row[0] == filter_identifier:
        # Split the string in the second column using whitespace
        if len(row) >= 2 and isinstance(row[1], str):
            values = row[1].split()
            for value in values:
                # Check if the value has already been processed for the current identifier
                if (row[0], value.lower()) not in processed_values.get(row[0], set()):
                    print((row[0], value, row[2]))
                    processed_values.setdefault(row[0], set()).add(value.lower())

# Close the cursor and connection
cursor.close()
connection.close()
