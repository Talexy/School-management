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
    print("\n===== TeachersDepartment Table =====")
    print("1.Assign teacher to department ")
    print("2. Remove teacher from department")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        teacher_id = input("Enter teacher ID:")
        department_id = input("Enter department ID:")

        cursor.execute(
            """
                      INSERT INTO TeacherDepartment (TeacherID, DepartmentID)
                      VALUES (?, ?)
        """,
            (teacher_id, department_id),
        )
        conn.commit()
        print("Teacher assigned to department successfully!")

    elif choice == "2":
        teacher_id = input("Enter teacher ID:")
        department_id = input("Enter department ID:")
        cursor.execute(
            """
                       DELETE FROM TeachersDepartment
                       WHERE TeacherID = ? AND DepartmentID = ?
                       """,
            (teacher_id, department_id),
        )
        conn.commit()
        print("Teacher removed from department successfully!")

    elif choice == "3":
        break

    else:
        print("Invalid choice!")

conn.close()
