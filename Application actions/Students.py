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
    print("\n===== Students Table =====")
    print("1. Create Students ")
    print("2. Edit Students ")
    print("3. Delete Students ")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        Student_ID = int(input("Enter Student ID: "))
        First_Name = input("Enter First Name: ")
        Last_Name = input("Enter Last Name: ")
        DateOfBirth = input("Enter Date Of Birth (YYYY-MM-DD): ")
        Stream_ID = int(input("Enter Stream ID: "))

        cursor.execute(
            """
       INSERT INTO Students (StudentID, FirstName, LastName, DateOfBirth, StreamID)
       VALUES (?, ?, ?, ?, ?)
       """,
            (Student_ID, First_Name, Last_Name, DateOfBirth, Stream_ID),
        )

        conn.commit()
        print("Students  created successfully!")

    elif choice == "2":
        Student_ID = int(input("Enter Student ID to edit: "))
        First_Name = input("Enter new First Name: ")
        Last_Name = input("Enter new Last Name: ")
        DateOfBirth = input("Enter new Date Of Birth (YYYY-MM-DD): ")
        Stream_ID = int(input("Enter new Stream ID: "))

        conn.execute(
            """
        UPDATE Students
        SET StudentID = ?, FirstName = ?, LastName = ?, DateOfBirth = ?, StreamID = ?
        WHERE StudentID = ?
        """,
            (Student_ID, First_Name, Last_Name, DateOfBirth, Stream_ID),
        )
        conn.commit()
        print("Students updated successfully!")

    elif choice == "3":
        Student_ID = int(input("Enter Student ID to delete: "))
        conn.execute("DELETE FROM Students WHERE StudentID = ?", (Student_ID,))
        conn.commit()
        print("Students deleted successfully!")

    elif choice == "4":
        break

    else:
        print("Invalid choice!")

conn.close()
