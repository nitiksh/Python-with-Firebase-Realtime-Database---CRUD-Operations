import firebase_admin
from firebase_admin import credentials, db
import json

# Initialize Firebase Realtime Database
def initialize_firebase():
    try:
        cred = credentials.Certificate("serviceAccountKey.json")  # Replace with your JSON file path
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://<your-database-name>.firebaseio.com/'  # Replace with your Firebase Realtime Database URL
        })
        print("Successfully connected to Firebase Realtime Database!")
    except Exception as e:
        print(f"Error initializing Firebase: {e}")
        exit()

# Add a new employee
def add_employee(employee_data):
    try:
        employee_name = employee_data["name"].lower()  # Using lowercase to standardize the key
        ref = db.reference('/employees')
        
        # Check if employee already exists
        if ref.child(employee_name).get():
            print(f"Error: Employee with name {employee_data['name']} already exists.")
            return

        ref.child(employee_name).set(employee_data)
        print(f"Employee {employee_data['name']} added successfully.")
    except Exception as e:
        print(f"Error adding employee: {e}")

# Update an existing employee
def update_employee(name, field, new_value):
    try:
        ref = db.reference(f'/employees/{name.lower()}')
        
        # Check if employee exists
        if not ref.get():
            print(f"Error: Employee {name} does not exist.")
            return
        
        ref.update({field: new_value})
        print(f"Employee {name} updated successfully: {field} -> {new_value}")
    except Exception as e:
        print(f"Error updating employee: {e}")

# Read employee data
def read_employee(name):
    try:
        ref = db.reference(f'/employees/{name.lower()}')
        
        employee_data = ref.get()
        
        if employee_data:
            print(json.dumps(employee_data, indent=4))
        else:
            print(f"Error: Employee {name} not found.")
    except Exception as e:
        print(f"Error reading employee data: {e}")

# Delete an employee
def delete_employee(name):
    try:
        ref = db.reference(f'/employees/{name.lower()}')
        
        # Check if employee exists
        if not ref.get():
            print(f"Error: Employee {name} does not exist.")
            return
        
        ref.delete()
        print(f"Employee {name} deleted successfully.")
    except Exception as e:
        print(f"Error deleting employee: {e}")

# Main menu to interact with the employee system
def main():
    while True:
        print("\nEmployee Management System - Admin Dashboard")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Read Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            name = input("Enter employee name: ").strip()
            age = input("Enter employee age: ").strip()
            position = input("Enter employee position: ").strip()
            department = input("Enter employee department: ").strip()
            salary = input("Enter employee salary: ").strip()
            
            employee_data = {
                "name": name,
                "age": age,
                "position": position,
                "department": department,
                "salary": salary
            }
            
            add_employee(employee_data)
        
        elif choice == "2":
            name = input("Enter employee name to update: ").strip()
            field = input("Enter field to update (age, position, department, salary): ").strip()
            new_value = input(f"Enter new value for {field}: ").strip()
            
            update_employee(name, field, new_value)
        
        elif choice == "3":
            name = input("Enter employee name to read: ").strip()
            read_employee(name)
        
        elif choice == "4":
            name = input("Enter employee name to delete: ").strip()
            delete_employee(name)
        
        elif choice == "5":
            print("Exiting the system.")
            break
        
        else:
            print("Invalid choice! Please try again.")

# Run the system
if __name__ == "__main__":
    initialize_firebase()
    main()