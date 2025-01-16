import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Realtime Database
def initialize_firebase():
    cred = credentials.Certificate("serviceAccountKey.json")  # Replace with your JSON file path
    firebase_admin.initialize_app(cred, {'databaseURL': 'https://<your-database-name>.firebaseio.com/'})

# Function to delete all data from the Firebase Realtime Database
def delete_all_data():
    ref = db.reference("/")  # Reference to the root of the database
    ref.delete()  # Delete all data
    print("All data has been deleted from the Firebase Realtime Database.")

# Main function
if __name__ == "__main__":
    initialize_firebase()  # Initialize Firebase
    delete_all_data()  # Delete all data from the Firebase Realtime Database