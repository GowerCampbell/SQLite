

# SQL Database Toolbox Tutorial in Python using SQLite

import sqlite3  # Import SQLite module (built-in in Python)

# Connect to (or create) a database
conn = sqlite3.connect("CompanyDB.db")  # Establish connection to SQLite database
cursor = conn.cursor()  # Create a cursor to execute SQL commands

# Data Definition Language (DDL)
# Defines the database structure, including tables and views.

# 1. Creating Tables (Schema)
# A schema defines the structure of the database including tables and relationships.

cursor.execute("""
CREATE TABLE IF NOT EXISTS Employees (
    EmployeeID INTEGER PRIMARY KEY,  # Unique identifier for each employee
    Name TEXT,  # Employee's name, equivalent to VARCHAR in SQL
    DepartmentID INTEGER,  # Foreign key referencing Departments table
    Salary REAL  # Employee's salary, equivalent to DECIMAL in SQL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Departments (
    DepartmentID INTEGER PRIMARY KEY,  # Unique identifier for each department
    DepartmentName TEXT  # Name of the department, equivalent to VARCHAR in SQL
)
""")

# Data Manipulation Language (DML)
# Performs CRUD operations: Create, Read, Update, Delete.


# 2. Inserting Data (CRUD - Create)
# CRUD stands for Create, Read, Update, and Delete. Here we insert data into tables.
cursor.execute("INSERT INTO Departments (DepartmentID, DepartmentName) VALUES (?, ?)", (1, "HR"))
cursor.execute("INSERT INTO Departments (DepartmentID, DepartmentName) VALUES (?, ?)", (2, "IT"))

cursor.execute("INSERT INTO Employees (EmployeeID, Name, DepartmentID, Salary) VALUES (?, ?, ?, ?)", (1, "Alice", 2, 60000))
cursor.execute("INSERT INTO Employees (EmployeeID, Name, DepartmentID, Salary) VALUES (?, ?, ?, ?)", (2, "Bob", 1, 50000))

conn.commit()  # Save changes to the database

# 3. Reading Data (CRUD - Read)
# SELECT statement retrieves data from the database.
cursor.execute("SELECT * FROM Employees")
print("Employees:")
print(cursor.fetchall())  # Fetch and print all employee records

# 4. Updating Data (CRUD - Update)
# UPDATE modifies existing records.
cursor.execute("UPDATE Employees SET Salary = ? WHERE EmployeeID = ?", (65000, 1))
conn.commit()

# 5. Deleting Data (CRUD - Delete)
# DELETE removes records from the database.
cursor.execute("DELETE FROM Employees WHERE EmployeeID = ?", (2,))
conn.commit()

# 6. Using Joins (SQL JOIN Equivalent)
# Joins combine rows from two or more tables based on a related column between them.
cursor.execute("""
SELECT Employees.Name, Departments.DepartmentName
FROM Employees
INNER JOIN Departments ON Employees.DepartmentID = Departments.DepartmentID
""")

print("Joined Data:")
print(cursor.fetchall())  # Fetch and display joined data

# 7. Creating a View (Virtual Table)
# A view is a virtual table based on a query result.
cursor.execute("""
CREATE VIEW IF NOT EXISTS EmployeeView AS
SELECT Name, Salary FROM Employees WHERE Salary > 50000
""")

# Fetch data from the view
cursor.execute("SELECT * FROM EmployeeView")
print("View Data:")
print(cursor.fetchall())  # Fetch and display view data

# 8. Indexing for Performance
# Indexing improves the speed of data retrieval operations.
cursor.execute("CREATE INDEX IF NOT EXISTS idx_employee_name ON Employees(Name)")

# Close the connection
conn.close()  # Always close the database connection after operations are complete


