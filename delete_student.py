import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Realtime Database
def initialize_firebase():
    cred = credentials.Certificate("serviceAccountKey.json")  # Replace with your JSON file path
    firebase_admin.initialize_app(cred, {'databaseURL': 'https://<your-database-name>.firebaseio.com/'})

# Function to fetch student data by name
def get_student_data_by_name(name):
    try:
        # Reference to the students node in Firebase
        ref = db.reference("/school/students")

        # Get all students' data
        students_data = ref.get()

        # Search for the student by name
        for student_id, student in students_data.items():
            if student['name'].lower() == name.lower():
                return student_id
        return None
    except Exception as e:
        print(f"Error fetching student data: {e}")
        return None

# Function to delete student data in Firebase
def delete_student_data(student_id):
    try:
        # Reference to the specific student node
        ref = db.reference(f"/school/students/{student_id}")
        ref.delete()  # Delete the student data
        print(f"Student with ID {student_id} deleted successfully.")
    except Exception as e:
        print(f"Error deleting student data: {e}")

# Main function to ask for student name and delete the student
def delete_student_info():
    # Ask the administrator for the student's name
    student_name = input("Enter the student's name to delete: ")

    # Fetch student data by name
    student_id = get_student_data_by_name(student_name)

    if student_id:
        print(f"Student {student_name} found. Proceeding to delete...")

        # Confirm deletion
        confirm = input(f"Are you sure you want to delete {student_name}'s data? (yes/no): ")
        if confirm.lower() == 'yes':
            delete_student_data(student_id)
        else:
            print("Deletion cancelled.")
    else:
        print(f"No student found with the name '{student_name}'.")

# Main execution
if __name__ == "__main__":
    initialize_firebase()  # Initialize Firebase
    delete_student_info()  # Delete student data
