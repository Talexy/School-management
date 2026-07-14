-- Create student's table 
CREATE TABLE Students (
    StudentID INT PRIMARY KEY,
    FirstName NVARCHAR(50) NOT NULL,
    LastName NVARCHAR(50) NOT NULL,
    DateOfBirth DATE NOT NULL,
    StreamID INT,
    FOREIGN KEY (StreamID) REFERENCES Streams(StreamID)
);
GO

--Create a teacher's table
CREATE TABLE Teachers (
    TeacherID INT PRIMARY KEY,
    FirstName NVARCHAR(50) NOT NULL,
    LastName NVARCHAR(50) NOT NULL,
    DateOfBirth DATE NOT NULL
);
GO  

--Create department table
CREATE TABLE Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName NVARCHAR(50) NOT NULL,
    HeadOfDepartment NVARCHAR(50) NOT NULL
);
GO

--Create a teachers department table
CREATE TABLE TeachersDepartment (
    TeacherID INT PRIMARY KEY,
    DepartmentID INT,
    FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID),
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);
GO

--Create a stream table
CREATE TABLE Streams (
    StreamID INT PRIMARY KEY,
    StreamName NVARCHAR(50) NOT NULL,
    TeacherID INT,
    FOREIGN KEY (TeacherID) REFERENCES Teachers(TeacherID),
    StreamCapacity NVARCHAR(50) NOT NULL
);
GO

--Create a subject table
CREATE TABLE Subjects (
    SubjectID INT PRIMARY KEY,
    SubjectName NVARCHAR(50) NOT NULL,
    DepartmentID INT,
    FOREIGN KEY (DepartmentID) REFERENCES Departments(DepartmentID)
);
GO

--Create a student's score table
CREATE TABLE Score (
    ScoreID INT PRIMARY KEY,
    StudentID INT,
    SubjectID INT,
    FOREIGN KEY (StudentID) REFERENCES Students(StudentID),
    FOREIGN KEY (SubjectID) REFERENCES Subjects(SubjectID),
    Score INT NOT NULL,
    Term NVARCHAR(50) NOT NULL,
    Year INT NOT NULL
);
GO

