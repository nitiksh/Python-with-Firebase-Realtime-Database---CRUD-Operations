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

# Add teachers data to Firebase classified by subjects
def add_teachers_to_firebase(teachers_by_subject, base_path="/school/teachers"):
    try:
        ref = db.reference(base_path)
        for subject, teachers in teachers_by_subject.items():
            subject_ref = ref.child(subject)  # Create a node for each subject
            for teacher in teachers:
                subject_ref.push(teacher)  # Push each teacher under the respective subject
        print(f"Teacher data successfully added to '{base_path}'!")
    except Exception as e:
        print("Error adding teacher data to Firebase:", e)

# Main Function
if __name__ == "__main__":
    initialize_firebase()

    # Teachers data classified by subjects
    teachers_by_subject = {
        "Mathematics": [
            {"name": "Alice Johnson", "email": "alice.math@example.com", "experience": 8, "age": 40},
            {"name": "Bob Carter", "email": "bob.math@example.com", "experience": 10, "age": 45}
        ],
        "Science": [
            {"name": "Charlie Brown", "email": "charlie.science@example.com", "experience": 6, "age": 35},
            {"name": "Diana Miller", "email": "diana.science@example.com", "experience": 12, "age": 50}
        ],
        "English": [
            {"name": "Evan Davis", "email": "evan.english@example.com", "experience": 5, "age": 30},
            {"name": "Fiona Harris", "email": "fiona.english@example.com", "experience": 15, "age": 55}
        ]
    }

    # Call the function to save teacher data
    add_teachers_to_firebase(teachers_by_subject)