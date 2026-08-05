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
    print("\n===== Teachers Table =====")
    print("1. Create Teachers ")
    print("2. Edit Teachers ")
    print("3. Delete Teachers")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        teacher_id = int(input("Enter Teacher ID: "))
        first_name = input("Enter First name: ")
        last_name = input("Enter Last name: ")
        date_of_birth = input("Enter Date Of Birth (YYYY-MM-DD): ")

        cursor.execute(
            """
            INSERT INTO Teachers (TeacherID, FirstName, LastName, DateOfBirth)
            VALUES (?, ?, ?, ?)
            """,
            (teacher_id, first_name, last_name, date_of_birth),
        )
        conn.commit()
        print("Teachers created successfully!")

    elif choice == "2":
        teacher_id = int(input("Enter teacher ID to edit: "))
        first_name = input("Enter new First name: ")
        last_name = input("Enter new Last Name: ")
        date_of_birth = input("Enter new Date Of Birth (YYYY-MM-DD): ")

        cursor.execute(
            """
            UPDATE Teachers
            SET FirstName = ?, LastName = ?, DateOfBirth = ?
            WHERE TeacherID = ?
            """,
            (first_name, last_name, date_of_birth, teacher_id),
        )
        conn.commit()
        print("Teachers updated successfully!")

    elif choice == "3":
        teacher_id = int(input("Enter teacher ID to delete: "))
        cursor.execute("DELETE FROM Teachers WHERE TeacherID = ?", (teacher_id,))
        conn.commit()
        print("Teachers deleted successfully!")

    elif choice == "4":
        break

    else:
        print("Invalid choice!")

conn.close()
