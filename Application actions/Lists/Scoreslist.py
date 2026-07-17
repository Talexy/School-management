import pyodbc

# Connect to SQL Server
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=SHEBYTES\\SQLEXPRESS;"
    "DATABASE=SchoolManagementDB;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

# -------- List Scores for students in a given stream -------- #

stream = input("Enter Stream Name: ").strip()

query_template = """
SELECT
    S.StudentID,
    S.FirstName,
    S.LastName,
    St.StreamName,
    Su.SubjectName,
    Sc.Score,
    Sc.Term,
    Sc.Year
FROM Students S
JOIN Streams St
    ON S.StreamID = St.StreamID
JOIN {score_table} Sc
    ON S.StudentID = Sc.StudentID
JOIN Subjects Su
    ON Sc.SubjectID = Su.SubjectID
WHERE St.StreamName = ?
ORDER BY S.StudentID, Su.SubjectName
"""

score_table = "Scores"

try:
    cursor.execute(query_template.format(score_table=score_table), (stream,))
except pyodbc.Error:
    score_table = "Score"
    cursor.execute(query_template.format(score_table=score_table), (stream,))

rows = cursor.fetchall()

if rows:
    print(f"\nScores for students in the '{stream}' stream")
    print("------------------------------------------------------------")

    current_student = None
    for row in rows:
        if row.StudentID != current_student:
            if current_student is not None:
                print()
            print(f"Student ID : {row.StudentID}")
            print(f"Name       : {row.FirstName} {row.LastName}")
            print(f"Stream     : {row.StreamName}")
            print("Scores:")
            current_student = row.StudentID

        print(f"  - {row.SubjectName}: {row.Score} ({row.Term} {row.Year})")

else:
    print(f"No score records found for stream '{stream}'.")

cursor.close()
conn.close()
