import pyodbc

# connect to sql server
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=SHEBYTES\\SQLEXPRESS;"
    "DATABASE=SchoolManagementDB;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

# ---------------- ADD STUDENT SCORE ---------------- #


def add_score():
    score_id = int(input("Enter Score ID: "))
    student_id = int(input("Enter Student ID: "))
    subject_id = int(input("Enter Subject ID: "))
    score = int(input("Enter Student Score: "))
    term = input("Enter Term: ")
    year = int(input("Enter Year: "))

    try:
        cursor.execute(
            """
        INSERT INTO Score
        (ScoreID, StudentID, SubjectID, Score, Term, Year)
        VALUES (?, ?, ?, ?, ?, ?)
        """,
            (score_id, student_id, subject_id, score, term, year),
        )

        conn.commit()
        print("\nStudent score added successfully!")

    except Exception as e:
        print("Error:", e)


# ---------------- EDIT STUDENT SCORE ---------------- #


def edit_score():
    score_id = int(input("Enter Score ID to edit: "))
    new_score = int(input("Enter New Score: "))
    new_term = input("Enter New Term: ")
    new_year = int(input("Enter New Year: "))

    try:
        cursor.execute(
            """
        UPDATE Score
        SET Score = ?,
            Term = ?,
            Year = ?
        WHERE ScoreID = ?
        """,
            (new_score, new_term, new_year, score_id),
        )

        conn.commit()

        if cursor.rowcount > 0:
            print("\nStudent score updated successfully!")
        else:
            print("\nScore ID not found.")

    except Exception as e:
        print("Error:", e)


# ---------------- MENU ---------------- #

while True:

    print("\n========== STUDENT SCORE MENU ==========")
    print("1. Add Student Score")
    print("2. Edit Student Score")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_score()

    elif choice == "2":
        edit_score()

    elif choice == "3":
        print("Program Closed.")
        break

    else:
        print("Invalid choice. Please try again.")

# ---------------- CLOSE CONNECTION ---------------- #

cursor.close()
conn.close()
