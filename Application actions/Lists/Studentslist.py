import pyodbc

# Connect to SQL Server
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=SHEBYTES\\SQLEXPRESS;"
    "DATABASE=SchoolManagementDB;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

# -------- List Students in a Stream -------- #

stream = input("Enter Stream Name: ")

cursor.execute(
    """
SELECT
    S.StudentID,
    S.FirstName,
    S.LastName,
    St.StreamName
FROM Students S
JOIN Streams St
    ON S.StreamID = St.StreamID
WHERE St.StreamName = ?
""",
    (stream,),
)

students = cursor.fetchall()

if students:
    print("\nStudents in", stream, "Stream")
    print("-----------------------------------------")

    for student in students:
        print(f"Student ID : {student.StudentID}")
        print(f"Name       : {student.FirstName} {student.LastName}")
        print()

else:
    print("No students found in that stream.")

cursor.close()
conn.close()
