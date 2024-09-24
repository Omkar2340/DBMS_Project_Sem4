import mysql.connector
from mysql.connector import Error
from datetime import date

# Function to create the database if it does not exist
def create_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="omkar",
            password="omkar123"
        )
        
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS EmployeeAttendance")
        print("Database 'EmployeeAttendance' created or already exists.")
    except Error as e:
        print(f"Error creating database: {e}")
    finally:
        cursor.close()
        conn.close()

# Function to create the Employees table
def create_employee_table():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="omkar",
            password="omkar123",
            database="EmployeeAttendance"
        )
        
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Employees (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                position VARCHAR(100),
                date_joined DATE,
                status ENUM('active', 'inactive') DEFAULT 'active'
            );
        """)
        conn.commit()
        print("Employees table created successfully.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

# Function to create the Attendance table
def create_attendance_table():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="omkar",
            password="omkar123",
            database="EmployeeAttendance"
        )
        
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Attendance (
                id INT AUTO_INCREMENT PRIMARY KEY,
                employee_id INT,
                attendance_date DATE,
                status ENUM('present', 'absent') NOT NULL,
                FOREIGN KEY (employee_id) REFERENCES Employees(id)
            );
        """)
        conn.commit()
        print("Attendance table created successfully.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

# Function to add an employee
def add_employee(name, position, date_joined):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="omkar",
            password="omkar123",
            database="EmployeeAttendance"
        )
        
        cursor = conn.cursor()
        sql = "INSERT INTO Employees (name, position, date_joined) VALUES (%s, %s, %s)"
        cursor.execute(sql, (name, position, date_joined))
        conn.commit()
        print("Employee added successfully.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

# Function to mark attendance
def mark_attendance(employee_id, status):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="omkar",
            password="omkar123",
            database="EmployeeAttendance"
        )
        
        cursor = conn.cursor()
        sql = "INSERT INTO Attendance (employee_id, attendance_date, status) VALUES (%s, %s, %s)"
        cursor.execute(sql, (employee_id, date.today(), status))
        conn.commit()
        print("Attendance marked successfully.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

# Function to get the total count of active employees
def get_employee_count():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="omkar",
            password="omkar123",
            database="EmployeeAttendance"
        )
        
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM Employees WHERE status='active'")
        count = cursor.fetchone()[0]
        return count
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

# Function to update employee details
def update_employee(emp_id, name=None, position=None, status=None):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="omkar",
            password="omkar123",
            database="EmployeeAttendance"
        )
        
        cursor = conn.cursor()
        updates = []
        if name:
            updates.append(f"name = '{name}'")
        if position:
            updates.append(f"position = '{position}'")
        if status:
            updates.append(f"status = '{status}'")
        
        update_str = ", ".join(updates)
        sql = f"UPDATE Employees SET {update_str} WHERE id = {emp_id}"
        cursor.execute(sql)
        conn.commit()
        print("Employee updated successfully.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

# Function to delete an employee
def delete_employee(emp_id):
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="omkar",
            password="omkar123",
            database="EmployeeAttendance"
        )
        
        cursor = conn.cursor()
        sql = "DELETE FROM Employees WHERE id = %s"
        cursor.execute(sql, (emp_id,))
        conn.commit()
        print("Employee deleted successfully.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

# Function to list all employees
def list_employees():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="omkar",
            password="omkar123",
            database="EmployeeAttendance"
        )
        
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Employees")
        employees = cursor.fetchall()
        
        for emp in employees:
            print(emp)
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

# Function to view attendance records for all employees
def view_all_attendance():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="omkar",
            password="omkar123",
            database="EmployeeAttendance"
        )
        
        cursor = conn.cursor()
        cursor.execute("""
            SELECT Employees.name, Attendance.attendance_date, Attendance.status 
            FROM Attendance 
            JOIN Employees ON Attendance.employee_id = Employees.id
        """)
        records = cursor.fetchall()
        
        if records:
            for record in records:
                print(f"Employee: {record[0]}, Date: {record[1]}, Status: {record[2]}")
        else:
            print("No attendance records found.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

# Main function to run the script
def main():
    create_database()  # Ensure the database is created first
    create_employee_table()
    create_attendance_table()
    
    while True:
        print("\n1. Add Employee")
        print("2. Mark Attendance")
        print("3. View Attendance")
        print("4. List Employees")
        print("5. Update Employee")
        print("6. Delete Employee")
        print("7. Get Active Employee Count")
        print("8. Exit")
        
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            name = input("Enter employee name: ")
            position = input("Enter employee position: ")
            date_joined = input("Enter date joined (YYYY-MM-DD): ")
            add_employee(name, position, date_joined)
        
        elif choice == '2':
            employee_id = int(input("Enter employee ID: "))
            status = input("Enter attendance status (present/absent): ")
            mark_attendance(employee_id, status)
        
        elif choice == '3':
            print("Attendance Records:")
            view_all_attendance()
        
        elif choice == '4':
            print("Current Employees:")
            list_employees()
        
        elif choice == '5':
            emp_id = int(input("Enter employee ID to update: "))
            name = input("Enter new name (leave blank to skip): ")
            position = input("Enter new position (leave blank to skip): ")
            status = input("Enter new status (active/inactive, leave blank to skip): ")
            update_employee(emp_id, name if name else None, position if position else None, status if status else None)
        
        elif choice == '6':
            emp_id = int(input("Enter employee ID to delete: "))
            delete_employee(emp_id)
        
        elif choice == '7':
            print(f'Total active employees: {get_employee_count()}')
        
        elif choice == '8':
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
