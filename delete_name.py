import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Realtime Database
def initialize_firebase():
    cred = credentials.Certificate("serviceAccountKey.json")  # Replace with your JSON file path
    firebase_admin.initialize_app(cred, {'databaseURL': 'https://<your-database-name>.firebaseio.com/'})

# Function to delete the name from Firebase if it exists
def delete_name_from_firebase():
    ref = db.reference("/names")  # Reference to '/names' path in Firebase
    name = ref.get()  # Get the current data at this reference
    
    if name:  # If data exists under '/names'
        ref.delete()  # Delete the name from Firebase
        print("The name has been deleted from Firebase.")
    else:
        print("No name found to delete in Firebase.")

# Main function
if __name__ == "__main__":
    initialize_firebase()  # Initialize Firebase
    
    # Delete the name from Firebase if it exists
    delete_name_from_firebase()