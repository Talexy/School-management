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
    print("1. Create Subjects")
    print("2. Edit Subjects")
    print("3. Delete Subjects")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        Subject_ID = int(input("Enter Subject ID: "))
        Subject_Name = input("Enter Subject Name: ")
        Department_ID = int(input("Enter Department ID: "))

        cursor.execute(
            """
        INSERT INTO Subjects (SubjectID, SubjectName, DepartmentID)
        VALUES (?, ?, ?)
        """,
            (Subject_ID, Subject_Name, Department_ID),
        )
        conn.commit()
        print("Subjects created successfully!")

    elif choice == "2":
        Subject_ID = int(input("Enter Subject ID to edit: "))
        Subject_Name = input("Enter new Subject Name: ")
        Department_ID = int(input("Enter new Department ID: "))

        cursor.execute(
            """
        UPDATE Subjects
        SET SubjectName = ?, DepartmentID = ?
        WHERE SubjectID = ?
        """,
            (Subject_Name, Department_ID, Subject_ID),
        )
        conn.commit()
        print("Subjects updated successfully!")

    elif choice == "3":
        Subject_ID = int(input("Enter Subject ID to delete: "))
        cursor.execute("DELETE FROM Subjects WHERE SubjectID = ?", (Subject_ID,))
        conn.commit()
        print("Subjects deleted successfully!")

    elif choice == "4":
        break

    else:
        print("Invalid choice!")

conn.close()
