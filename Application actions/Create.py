import pyodbc

# Connect to SQL Server
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=SHEBYTES\\SQLEXPRESS;"
    "DATABASE=SchoolManagementDB;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

while True:
    print("\n===== DATABASE MENU =====")
    print("1. Create Table")
    print("2. Edit Table (Add Column)")
    print("3. Delete Table")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        table_name = input("Enter table name: ")

        sql = f"""
        CREATE TABLE {table_name}(
            ID INT PRIMARY KEY,
            Name NVARCHAR(50)
        )
        """

        cursor.execute(sql)
        conn.commit()
        print("Table created successfully!")

    elif choice == "2":
        table_name = input("Enter table name: ")
        column_name = input("Enter new column name: ")

        sql = f"""
        ALTER TABLE {table_name}
        ADD {column_name} NVARCHAR(50)
        """

        cursor.execute(sql)
        conn.commit()
        print("Table updated successfully!")

    elif choice == "3":
        table_name = input("Enter table name to delete: ")

        sql = f"DROP TABLE {table_name}"

        cursor.execute(sql)
        conn.commit()
        print("Table deleted successfully!")

    elif choice == "4":
        break

    else:
        print("Invalid choice!")

conn.close()