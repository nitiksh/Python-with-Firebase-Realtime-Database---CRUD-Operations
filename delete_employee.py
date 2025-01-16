import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Realtime Database
def initialize_firebase():
    cred = credentials.Certificate("serviceAccountKey.json")  # Replace with your JSON file path
    firebase_admin.initialize_app(cred, {'databaseURL': 'https://<your-database-name>.firebaseio.com/'})

# Function to add employee data
def add_employee(name, age, position):
    ref = db.reference("/employee")  # Reference to '/employee' node in Firebase
    new_employee_ref = ref.push()  # Push new employee data
    new_employee_ref.set({
        'name': name,
        'age': age,
        'position': position
    })
    print(f"Employee {name} added successfully.")

# Function to delete employee by name
def delete_employee_by_name(name):
    ref = db.reference("/employee")  # Reference to '/employee' node in Firebase
    employees = ref.get()  # Get all employee data
    
    if employees:
        for employee_id, employee_data in employees.items():
            if employee_data['name'].lower() == name.lower():  # Check for matching name (case-insensitive)
                employee_ref = ref.child(employee_id)  # Reference to the specific employee node
                employee_ref.delete()  # Delete the employee
                print(f"Employee {name} has been deleted.")
                return
        print(f"Employee {name} not found.")
    else:
        print("No employees found.")

# Main function
if __name__ == "__main__":
    initialize_firebase()  # Initialize Firebase

    # Adding sample employee data
    add_employee("Alice", 30, "Manager")
    add_employee("Bob", 40, "Developer")
    add_employee("Charlie", 35, "Designer")

    # Delete an employee by name
    delete_employee_by_name("Bob")  # Change this to the name you want to delete