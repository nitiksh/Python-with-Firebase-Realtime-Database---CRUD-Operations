import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Realtime Database
def initialize_firebase():
    cred = credentials.Certificate("serviceAccountKey.json")  # Replace with your JSON file path
    firebase_admin.initialize_app(cred, {'databaseURL': 'https://<your-database-name>.firebaseio.com/'})

# Function to add name to Firebase
def add_name_to_firebase():
    ref = db.reference("/names")  # Reference to '/names' path in Firebase
    ref.set("John Doe")  # Add initial name to Firebase

# Function to update name in Firebase
def update_name_in_firebase(new_name):
    ref = db.reference("/names")  # Reference to '/names' path in Firebase
    ref.set(new_name)  # Update name in Firebase

# Function to print the name stored in Firebase
def print_name_from_firebase():
    ref = db.reference("/names")  # Reference to '/names' path in Firebase
    name = ref.get()  # Fetch the data
    print("Current Name in Firebase:", name)

# Main function
if __name__ == "__main__":
    initialize_firebase()  # Initialize Firebase
    
    # Step 1: Add name to Firebase
    add_name_to_firebase()
    print("Added name to Firebase:")
    print_name_from_firebase()  # Print the name after adding

    # Step 2: Update name to "Jane Doe"
    update_name_in_firebase("Jane Doe")
    print("\nUpdated name to 'Jane Doe':")
    print_name_from_firebase()  # Print the name after first update

    # Step 3: Update name again to "Alice Smith"
    update_name_in_firebase("Alice Smith")
    print("\nUpdated name to 'Alice Smith':")
    print_name_from_firebase()  # Print the name after second update