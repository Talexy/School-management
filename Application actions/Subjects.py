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
    print("\n===== Subjects Table =====")
    print("1. Create Subjects Table")
    print("2. Edit Subjects Table")
    print("3. Delete Subjects Table")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        cursor.execute("""
        CREATE TABLE Subjects
    (
           TeacherID NVARCHAR(50) PRIMARY KEY,
           FirstName NVARCHAR(50),
           LastName NVARCHAR(50),
           DateOfBirth DATE            
        )
        """)
        conn.commit()
        print("Subjects table created successfully!")

    elif choice == "2":
        column_name = input("Enter new column name:")
        datatype = input("Enter data type:")
        cursor.execute(f"ALTER TABLE Subjects ADD {column_name} {datatype}")
        conn.commit()
        print("Column added successfully!")

    elif choice == "3":
        cursor.execute("DROP TABLE Subjects ")
        conn.commit()
        print("Subjects table deleted successfully!")

    elif choice == "4":
        break

    else:
        print("Invalid choice!")

conn.close()
