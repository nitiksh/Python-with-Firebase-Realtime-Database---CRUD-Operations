import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Realtime Database
def initialize_firebase():
    cred = credentials.Certificate("serviceAccountKey.json")  # Replace with your JSON file path
    firebase_admin.initialize_app(cred, {'databaseURL': 'https://<your-database-name>.firebaseio.com/'})

# Function to add a name to Firebase
def add_name_to_firebase(name):
    ref = db.reference("/names")  # Reference to '/names' path in Firebase
    ref.set(name)  # Add the name to Firebase

# Main function
if __name__ == "__main__":
    initialize_firebase()  # Initialize Firebase
    
    # Input name dynamically
    name = input("Enter a name to add to Firebase: ")
    
    # Add the name to Firebase
    add_name_to_firebase(name)
    
    print(f"Name '{name}' has been added to Firebase.")