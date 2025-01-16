import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Realtime Database
def initialize_firebase():
    try:
        cred = credentials.Certificate("serviceAccountKey.json")  # Replace with your JSON file path
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://<your-database-name>.firebaseio.com/'
        })
        print("Successfully connected to Firebase Realtime Database!")
    except Exception as e:
        print("Error initializing Firebase:", e)
        exit()

# Add employee data to Firebase
def add_employees_to_firebase(employees, base_path="/employees"):
    try:
        ref = db.reference(base_path)
        for employee in employees:
            ref.push(employee)  # Push each employee to the database with a unique key
        print(f"Employee data successfully added to '{base_path}'!")
    except Exception as e:
        print("Error adding employee data to Firebase:", e)

# Main Function
if __name__ == "__main__":
    initialize_firebase()

    # Employees data as a JSON list
    employees = [
        {"name": "Alice", "email": "alice@example.com", "position": "Software Developer", "age": 28},
        {"name": "Bob", "email": "bob@example.com", "position": "Project Manager", "age": 35},
        {"name": "Charlie", "email": "charlie@example.com", "position": "UI/UX Designer", "age": 25},
        {"name": "Diana", "email": "diana@example.com", "position": "DevOps Engineer", "age": 30}
    ]

    # Call the function to save employee data
    add_employees_to_firebase(employees)