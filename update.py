import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Realtime Database
def initialize_firebase():
    cred = credentials.Certificate("serviceAccountKey.json")  # Replace with your JSON file path
    firebase_admin.initialize_app(cred, {'databaseURL': 'https://<your-database-name>.firebaseio.com/'})

# Function to create and set data in Firebase
def create_data():
    data = {
        "user1": {"name": "Alice", "age": 25},
        "user2": {"name": "Bob", "age": 30}
    }
    ref = db.reference("/users")  # Reference to '/users' path in Firebase
    ref.set(data)  # Push the initial data

# Function to read and print data from Firebase
def print_data():
    ref = db.reference("/users")  # Reference to '/users' path in Firebase
    users_data = ref.get()  # Fetch the data
    print("Data from Firebase:")
    print(users_data)  # Print fetched data

# Function to update data in Firebase
def update_data():
    ref = db.reference("/users/user1")  # Reference to user1's data in Firebase
    ref.update({"age": 26})  # Update the age of user1

# Main function
if __name__ == "__main__":
    initialize_firebase()  # Initialize Firebase
    
    # Step 1: Create data
    create_data()
    print("Initial Data:")
    print_data()  # Print the initial data
    
    # Step 2: Update data
    update_data()
    print("\nUpdated Data:")
    print_data()  # Print the updated data