import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Realtime Database
def initialize_firebase():
    cred = credentials.Certificate("serviceAccountKey.json")  # Replace with your JSON file path
    firebase_admin.initialize_app(cred, {'databaseURL': 'https://<your-database-name>.firebaseio.com/'})

# Function to fetch student data by name
def get_student_data_by_name(name):
    # Reference to the students node in Firebase
    ref = db.reference("/school/students")

    # Get all students' data
    students_data = ref.get()

    # Search for the student by name
    for student_id, student in students_data.items():
        if student['name'].lower() == name.lower():
            return student
    return None

# Main function to ask for student name and display the data
def read_student_data():
    # Ask the administrator for the student's name
    student_name = input("Enter the student's name to search: ")

    # Fetch student data by name
    student_data = get_student_data_by_name(student_name)

    if student_data:
        print("\nStudent Data Found:")
        print(f"Name: {student_data['name']}")
        print(f"Gender: {student_data['gender']}")
        print(f"Age: {student_data['age']}")
        print(f"Course: {student_data['course']}")
    else:
        print(f"No student found with the name '{student_name}'.")

# Main execution
if __name__ == "__main__":
    initialize_firebase()  # Initialize Firebase
    read_student_data()  # Read student data by name