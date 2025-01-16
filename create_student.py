import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Realtime Database
def initialize_firebase():
    cred = credentials.Certificate("serviceAccountKey.json")  # Replace with your JSON file path
    firebase_admin.initialize_app(cred, {'databaseURL': 'https://<your-database-name>.firebaseio.com/'})

# Function to add a new student admission to Firebase
def add_student_admission():
    # Ask user for student details
    print("Enter the student's details:")
    name = input("Name: ")
    gender = input("Gender: ")
    age = input("Age: ")
    course = input("Course: ")

    # Create a dictionary for the student
    student_data = {
        'name': name,
        'gender': gender,
        'age': age,
        'course': course
    }

    # Reference to the students node in Firebase
    ref = db.reference("/school/students")

    # Add the student data to the students node with a unique ID
    student_ref = ref.push(student_data)

    # Print confirmation
    print(f"Student '{name}' has been added successfully with ID: {student_ref.key}")

# Main function
if __name__ == "__main__":
    initialize_firebase()  # Initialize Firebase
    add_student_admission()  # Add student admission to Firebase