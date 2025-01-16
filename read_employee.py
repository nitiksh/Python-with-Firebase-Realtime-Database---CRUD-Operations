import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Realtime Database
def initialize_firebase():
    cred = credentials.Certificate("serviceAccountKey.json")  # Replace with your JSON file path
    firebase_admin.initialize_app(cred, {'databaseURL': 'https://<your-database-name>.firebaseio.com/'})

# Function to create nested employee data
def create_employee_data():
    employees = {
        "HR": {
            "employees": {
                "E001": {"name": "Alice Smith", "age": 29, "position": "HR Manager", "salary": 60000},
                "E002": {"name": "John Doe", "age": 35, "position": "HR Assistant", "salary": 40000}
            }
        },
        "Engineering": {
            "employees": {
                "E003": {"name": "Charlie Brown", "age": 40, "position": "Software Engineer", "salary": 80000},
                "E004": {"name": "Diana White", "age": 32, "position": "QA Engineer", "salary": 70000}
            }
        },
        "Sales": {
            "employees": {
                "E005": {"name": "Evan Black", "age": 45, "position": "Sales Manager", "salary": 90000},
                "E006": {"name": "Fiona Green", "age": 38, "position": "Sales Executive", "salary": 55000}
            }
        }
    }
    
    ref = db.reference("/company/employees")  # Reference to company/employees in Firebase
    ref.set(employees)  # Push the employee data into Firebase

# Function to read nested employee data
def read_employee_data():
    ref = db.reference("/company/employees")  # Reference to company/employees in Firebase
    employees_data = ref.get()  # Fetch the data from Firebase
    
    print("Employee Data by Department:")
    for department, data in employees_data.items():
        print(f"Department: {department}")
        for emp_id, emp_info in data['employees'].items():
            print(f"  Employee ID: {emp_id}")
            print(f"    Name: {emp_info['name']}")
            print(f"    Age: {emp_info['age']}")
            print(f"    Position: {emp_info['position']}")
            print(f"    Salary: {emp_info['salary']}")
            print("-" * 30)

# Main function
if __name__ == "__main__":
    initialize_firebase()  # Initialize Firebase
    create_employee_data()  # Create employee data
    read_employee_data()    # Read and display employee data