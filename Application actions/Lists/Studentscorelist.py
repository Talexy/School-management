import pyodbc

# Connect to SQL Server

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=SHEBYTES\\SQLEXPRESS;"
    "DATABASE=SchoolManagementDB;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

# ---------------- LIST STUDENT SCORES ---------------- #

student_id = int(input("Enter Student ID: "))

cursor.execute(
    """
SELECT
    S.StudentID,
    S.FirstName,
    S.LastName,
    Sub.SubjectName,
    Sc.Score,
    Sc.Term,
    Sc.Year
FROM Students S
JOIN Scores Sc
    ON S.StudentID = Sc.StudentID
JOIN Subjects Sub
    ON Sc.SubjectID = Sub.SubjectID
WHERE S.StudentID = ?
ORDER BY Sc.Year, Sc.Term, Sub.SubjectName
""",
    (student_id,),
)

records = cursor.fetchall()

if records:
    print("\n========== STUDENT SCORES ==========\n")

    print(f"Student ID   : {records[0].StudentID}")
    print(f"Student Name : {records[0].FirstName} {records[0].LastName}")
    print()

    print(f"{'Subject':<20}{'Score':<10}{'Term':<12}{'Year'}")
    print("-" * 50)

    for row in records:
        print(f"{row.SubjectName:<20}{row.Score:<10}{row.Term:<12}{row.Year}")

else:
    print("No scores found for this student.")

cursor.close()
conn.close()
