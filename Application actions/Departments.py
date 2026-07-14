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
    print("\n===== Departments Table =====")
    print("1. Create Departments Table")
    print("2. Edit Departments Table")
    print("3. Delete Departments Table")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        cursor.execute("""
        CREATE TABLE Departments(
            DepartmentID NVARCHAR(50) PRIMARY KEY,
            DepartmentName NVARCHAR(50),
            HeadOfDepartment NVARCHAR(50)
        )
        """)
        conn.commit()
        print("Departments table created successfully!")

    elif choice == "2":
        column_name = input("Enter new column name:")
        datatype = input("Enter data type:")
        cursor.execute(f"ALTER TABLE Departments ADD {column_name} {datatype}")
        conn.commit()
        print("Column added successfully!")

    elif choice == "3":
        cursor.execute("DROP TABLE Departments")
        conn.commit()
        print("Departments table deleted successfully!")

    elif choice == "4":
        break

    else:
        print("Invalid choice!")

conn.close()
