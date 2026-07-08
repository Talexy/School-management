import pyodbc

# connect to sql server
conn = pyodbc.connect(
    "DRIVER={ODBC DRIVER 17 for SQL Server};"
    "SERVER=SHEBYTES\\SQLEXPRESS;"
    "DATABASE=SchoolManagementDB;"
    "Trusted_Connection=yes;"
)
cursor = conn.cursor()

while True:
    print("\n===== Stream Table =====")
    print("1. Create Stream Table")
    print("2. Edit Stream Table")
    print("3. Delete Stream Table")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        cursor.execute("""
        CREATE TABLE Stream

    (
           TeacherID INT PRIMARY KEY,
           FirstName NVARCHAR(50),
           LastName NVARCHAR(50),
           DateOfBirth DATE            
        )
        """)
        conn.commit()
        print("Stream table created successfully!")

    elif choice == "2":
        column_name = input("Enter new column name:")
        datatype = input("Enter data type:")
        cursor.execute(f"ALTER TABLE Stream ADD {column_name} {datatype}")
        conn.commit()
        print("Column added successfully!")

    elif choice == "3":
        cursor.execute("DROP TABLE Stream ")
        conn.commit()
        print("Stream table deleted successfully!")

    elif choice == "4":
        break

    else:
        print("Invalid choice!")

conn.close()
