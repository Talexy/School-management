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
    print("\n===== Streams Table =====")
    print("1. Create new Stream ")
    print("2. Edit Stream ")
    print("3. Delete Stream ")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        Stream_ID = input("Enter new Stream ID: ")
        Stream_Name = input("Enter stream Name: ")
        Teacher_ID = input("Enter teacher ID: ")
        Stream_Capacity = input("Enter stream capacity: ")

        cursor.execute(
            """
       INSERT INTO Streams( StreamID, StreamName, TeacherID, StreamCapacity)
       VALUES (?, ?, ?, ?)
        """,
            (Stream_ID, Stream_Name, Teacher_ID, Stream_Capacity),
        )
        conn.commit()
        print("New Stream created successfully!")

    elif choice == "2":
        Stream_ID = input("Enter Stream ID to edit: ")
        Stream_Name = input("Enter new stream Name: ")
        Teacher_ID = input("Enter teacher ID: ")
        Stream_Capacity = input("Enter stream capacity: ")

        cursor.execute(
            """
               UPDATE Streams
               SET StreamID = ?, StreamName = ?, TeacherID = ?, StreamCapacity = ?
               WHERE StreamID = ?
               """,
            (Stream_ID, Stream_Name, Teacher_ID, Stream_Capacity, Stream_ID),
        )
        conn.commit()
        print("Stream updated successfully!")

    elif choice == "3":
        Stream_ID = input("Enter Stream ID to delete: ")
        cursor.execute("DELETE FROM Streams WHERE StreamID = ?", (Stream_ID,))
        conn.commit()
        print("Stream deleted successfully!")

    elif choice == "4":
        break

    else:
        print("Invalid choice!")

conn.close()
