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
                return student_id, student
        return None, None
    except Exception as e:
        print(f"Error fetching student data: {e}")
        return None, None

# Function to update student data in Firebase
def update_student_data(student_id, field, new_value):
    try:
        # Reference to the specific student node
        ref = db.reference(f"/school/students/{student_id}")
        ref.update({field: new_value})
        print(f"{field} updated successfully to {new_value}")
    except Exception as e:
        print(f"Error updating student data: {e}")

# Main function to ask for student name and allow updates
def update_student_info():
    # Ask the administrator for the student's name
    student_name = input("Enter the student's name to search: ")

    # Fetch student data by name
    student_id, student_data = get_student_data_by_name(student_name)

    if student_data:
        print("\nStudent Data Found:")
        print(f"Name: {student_data['name']}")
        print(f"Gender: {student_data['gender']}")
        print(f"Age: {student_data['age']}")
        print(f"Course: {student_data['course']}")

        # Ask which field to update
        print("\nWhich field would you like to update?")
        print("1. Name")
        print("2. Gender")
        print("3. Age")
        print("4. Course")
        choice = input("Enter the number of the field to update (or 'exit' to quit): ")

        # Handle the user's choice
        if choice == '1':
            new_name = input("Enter the new name: ")
            update_student_data(student_id, 'name', new_name)
        elif choice == '2':
            new_gender = input("Enter the new gender: ")
            update_student_data(student_id, 'gender', new_gender)
        elif choice == '3':
            new_age = input("Enter the new age: ")
            update_student_data(student_id, 'age', new_age)
        elif choice == '4':
            new_course = input("Enter the new course: ")
            update_student_data(student_id, 'course', new_course)
        elif choice.lower() == 'exit':
            print("Exiting the update process.")
        else:
            print("Invalid choice. Please try again.")

    else:
        print(f"No student found with the name '{student_name}'.")

# Main execution
if __name__ == "__main__":
    initialize_firebase()  # Initialize Firebase
    update_student_info()  # Read and update student data
