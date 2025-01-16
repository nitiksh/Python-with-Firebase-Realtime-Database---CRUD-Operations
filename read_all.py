import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Realtime Database
def initialize_firebase():
    cred = credentials.Certificate("serviceAccountKey.json")  # Replace with your JSON file path
    firebase_admin.initialize_app(cred, {'databaseURL': 'https://<your-database-name>.firebaseio.com/'})

# Function to read all data from Firebase Realtime Database
def read_all_data():
    ref = db.reference("/")  # Reference to the root of the database
    data = ref.get()  # Get all the data from the database
    print("All Data from Firebase Realtime Database:")
    print(data)  # Print all data

# Main function
if __name__ == "__main__":
    initialize_firebase()  # Initialize Firebase
    read_all_data()  # Read and print all data from Firebase Realtime Database