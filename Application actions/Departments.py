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
    print("1. Add Departments ")
    print("2. Edit Departments ")
    print("3. Delete Departments ")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        Department_ID = int(input("Enter Department ID  : "))
        Department_Name = input("Enter Department name : ")
        HeadOfDepartment = input("Enter head of department : ")

        cursor.execute(
            """
        INSERT INTO Departments
        (DepartmentID, DepartmentName, HeadOfDepartment)
        VALUES (?, ?, ?)
        """,
            (Department_ID, Department_Name, HeadOfDepartment),
        )

        conn.commit()
        print("Department created successfully!")

    elif choice == "2":
        Department_ID = int(input("Enter Department ID to edit: "))
        Department_Name = input("Enter new department name: ")
        HeadOfDepartment = input("Enter new head of department: ")

        cursor.execute(
            """
        UPDATE Departments
        SET DepartmentName = ?, HeadOfDepartment = ?
        WHERE DepartmentID = ?
        """,
            (Department_Name, HeadOfDepartment, Department_ID),
        )
        conn.commit()
        print("Department updated successfully!")

    elif choice == "3":
        Department_ID = int(input("Enter Department ID to delete: "))
        cursor.execute(
            "DELETE FROM Departments WHERE DepartmentID = ?", (Department_ID,)
        )
        conn.commit()
        print("Departments deleted successfully!")

    elif choice == "4":
        break

    else:
        print("Invalid choice!")

conn.close()
