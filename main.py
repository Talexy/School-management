import pyodbc

# Connect to SQL Server
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=SHEBYTES\\SQLEXPRESS;"
    "DATABASE=SchoolManagementDB;"
    "Trusted_Connection=yes;"
)

# Create a cursor
cursor = conn.cursor()

print("Connected successfully to SchoolManagementDB!")

# Close the connection
conn.close()