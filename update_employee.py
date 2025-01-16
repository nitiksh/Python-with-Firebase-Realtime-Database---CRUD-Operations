import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Realtime Database
def initialize_firebase():
    cred = credentials.Certificate("serviceAccountKey.json")  # Replace with your JSON file path
    firebase_admin.initialize_app(cred, {'databaseURL': 'https://<your-database-name>.firebaseio.com/'})

# Function to create and set employee data in Firebase
def create_employee_data():
    employees = {
        "emp1": {"name": "John Doe", "position": "Software Engineer", "age": 28, "department": "Engineering", "salary": 60000},
        "emp2": {"name": "Jane Smith", "position": "Product Manager", "age": 35, "department": "Product", "salary": 80000}
    }
    ref = db.reference("/employees")  # Reference to '/employees' path in Firebase
    ref.set(employees)  # Push the initial employee data

# Function to read and print employee data from Firebase
def print_employee_data():
    ref = db.reference("/employees")  # Reference to '/employees' path in Firebase
    employees_data = ref.get()  # Fetch the data
    print("Employee Data from Firebase:")
    print(employees_data)  # Print fetched employee data

# Function to update employee data in Firebase
def update_employee_data():
    # Updated full details for emp1 and emp2
    updated_data = {
        "emp1": {"name": "Johnathan Doe", "position": "Lead Software Engineer", "age": 30, "department": "Engineering", "salary": 85000},
        "emp2": {"name": "Janet Smith", "position": "Senior Product Manager", "age": 38, "department": "Product", "salary": 95000}
    }
    
    ref = db.reference("/employees")  # Reference to '/employees' path in Firebase
    ref.set(updated_data)  # Update all employee details for both emp1 and emp2

# Main function
if __name__ == "__main__":
    initialize_firebase()  # Initialize Firebase
    
    # Step 1: Create employee data
    create_employee_data()
    print("Initial Employee Data:")
    print_employee_data()  # Print the initial employee data
    
    # Step 2: Update employee data
    update_employee_data()
    print("\nUpdated Employee Data:")
    print_employee_data()  # Print the updated employee data