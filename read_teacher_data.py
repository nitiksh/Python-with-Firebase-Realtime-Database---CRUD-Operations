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

# Function to read teacher data from Firebase
def read_teachers_from_firebase(base_path="/school/teachers"):
    try:
        ref = db.reference(base_path)
        teachers_data = ref.get()  # Fetch all data from the reference

        if teachers_data:
            print("Teacher Data by Subject:\n")
            for subject, teachers in teachers_data.items():
                print(f"<-----------{subject}------------>")
                for teacher_id, teacher in teachers.items():
                    print(f"-->  Name: {teacher['name']}")
                    print(f"-->  Email: {teacher['email']}")
                    print(f"-->  Experience: {teacher['experience']} years")
                    print(f"-->  Age: {teacher['age']} years\n")
        else:
            print("No teacher data found.")

    except Exception as e:
        print("Error reading teacher data from Firebase:", e)

# Main Function
if __name__ == "__main__":
    initialize_firebase()

    # Read and display teacher data
    read_teachers_from_firebase()
