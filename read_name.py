import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Realtime Database
def initialize_firebase():
    cred = credentials.Certificate("serviceAccountKey.json")  # Replace with your JSON file path
    firebase_admin.initialize_app(cred, {'databaseURL': 'https://<your-database-name>.firebaseio.com/'})

# Function to read the name from Firebase
def read_name_from_firebase():
    ref = db.reference("/names")  # Reference to '/names' path in Firebase
    name = ref.get()  # Get the data at this reference
    return name

# Main function
if __name__ == "__main__":
    initialize_firebase()  # Initialize Firebase
    
    # Read the name from Firebase
    name = read_name_from_firebase()
    
    if name:
        print(f"The name stored in Firebase is: {name}")
    else:
        print("No name found in Firebase.")