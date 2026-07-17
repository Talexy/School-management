import pyodbc

# Connect to SQL Server
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=SHEBYTES\\SQLEXPRESS;"
    "DATABASE=SchoolManagementDB;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

# -------- List Teachers in a Department -------- #

department = input("Enter Department Name: ")

cursor.execute(
    """
SELECT
    T.TeacherID,
    T.FirstName,
    T.LastName,
    D.DepartmentName
FROM Teachers T
JOIN TeachersDepartment TD
    ON T.TeacherID = TD.TeacherID
JOIN Departments D
    ON TD.DepartmentID = D.DepartmentID
WHERE D.DepartmentName = ?
""",
    (department,),
)

teachers = cursor.fetchall()

if teachers:
    print("\nTeachers in", department, "Department")
    print("-----------------------------------------")

    for teacher in teachers:
        print(f"Teacher ID : {teacher.TeacherID}")
        print(f"Name       : {teacher.FirstName} {teacher.LastName}")
        print()

else:
    print("No teachers found in that department.")

cursor.close()
conn.close()
