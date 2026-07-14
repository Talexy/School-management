import pyodbc
import csv

# ---------------- CONNECT TO SQL SERVER ---------------- #

try:
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=SHEBYTES\\SQLEXPRESS;"
        "DATABASE=SchoolManagementDB;"
        "Trusted_Connection=yes;"
    )

    cursor = conn.cursor()
    print("Connected to SQL Server successfully!\n")

except Exception as e:
    print("Connection failed!")
    print(e)
    exit()


# ---------------- LOAD TEACHERS ---------------- #


def load_teachers():
    with open("Teachers.csv", "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            print(row)
            cursor.execute(
                "INSERT INTO Teachers (TeacherID, FirstName, LastName, DateOfBirth) VALUES (?,?,?,?)",
                row,
            )

    print("Teachers imported successfully.")


# ---------------- LOAD DEPARTMENTS ---------------- #


def load_departments():
    with open("Departments.csv", "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            cursor.execute(
                "INSERT INTO Departments (DepartmentID, DepartmentName, HeadOfDepartment) VALUES (?,?,?)",
                row,
            )

    print("Departments imported successfully.")


# ---------------- LOAD STREAMS ---------------- #


def load_streams():
    with open("Streams.csv", "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            cursor.execute(
                "INSERT INTO Streams (StreamID, StreamName, TeacherID, StreamCapacity) VALUES (?,?,?,?)",
                row,
            )

    print("Streams imported successfully.")


# ---------------- LOAD STUDENTS ---------------- #


def load_students():
    with open("Students.csv", "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            cursor.execute(
                "INSERT INTO Students (StudentID, FirstName, LastName, DateOfBirth, StreamID) VALUES (?,?,?,?,?)",
                row,
            )

    print("Students imported successfully.")


# ---------------- LOAD SUBJECTS ---------------- #


def load_subjects():
    with open("Subjects.csv", "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            cursor.execute(
                "INSERT INTO Subjects (SubjectID, SubjectName, DepartmentID) VALUES (?,?,?)",
                row,
            )

    print("Subjects imported successfully.")


# ---------------- LOAD TEACHERS DEPARTMENT ---------------- #


def load_teachers_departments():
    with open("TeachersDepartment.csv", "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            cursor.execute(
                "INSERT INTO TeachersDepartment (TeacherID, DepartmentID) VALUES (?,?)",
                row,
            )

    print("TeachersDepartment imported successfully.")


# ---------------- LOAD SCORES ---------------- #


def load_scores():
    with open("Scores.csv", "r", newline="") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            cursor.execute(
                "INSERT INTO Scores (ScoreID, StudentID, SubjectID, Score, Term, Year) VALUES (?,?,?,?,?,?)",
                row,
            )

    print("Scores imported successfully.")


# ---------------- MAIN ---------------- #

try:
    load_teachers()
    conn.commit()
    load_departments()
    conn.commit()
    load_streams()
    conn.commit()
    load_students()
    conn.commit()
    load_subjects()
    conn.commit()
    load_teachers_departments()
    conn.commit()
    load_scores()

    conn.commit()

    print("\n===================================")
    print("All CSV data imported successfully!")
    print("===================================")

except Exception as e:
    conn.rollback()
    print("\nAn error occurred:")
    print(e)

finally:
    cursor.close()
    conn.close()
