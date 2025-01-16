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

# Create or Add Data
def create_data(path, data):
    try:
        ref = db.reference(path)
        new_ref = ref.push(data)  # Automatically generates a unique key
        print(f"Data added successfully at key: {new_ref.key}")
    except Exception as e:
        print("Error creating data:", e)

# Read Data
def read_data(path):
    try:
        ref = db.reference(path)
        data = ref.get()
        if data:
            print(f"Data at '{path}':", data)
        else:
            print(f"No data found at '{path}'")
    except Exception as e:
        print("Error reading data:", e)

# Update Data
def update_data(path, updates):
    try:
        ref = db.reference(path)
        ref.update(updates)
        print(f"Data at '{path}' updated successfully!")
    except Exception as e:
        print("Error updating data:", e)

# Delete Data
def delete_data(path):
    try:
        ref = db.reference(path)
        ref.delete()
        print(f"Data at '{path}' deleted successfully!")
    except Exception as e:
        print("Error deleting data:", e)

# Main Function (Example Usage)
if __name__ == "__main__":
    initialize_firebase()

    # Create (Add Data)
    create_data("/users", {"name": "Alice", "email": "alice@example.com", "age": 25})
    create_data("/users", {"name": "Bob", "email": "bob@example.com", "age": 30})

    # Read Data
    read_data("/users")

    # Update Data
    update_data("/users/-UniqueKeyHere", {"name": "Alice Updated"})  # Replace -UniqueKeyHere with the actual key

    # Delete Data
    delete_data("/users/-UniqueKeyHere")  # Replace -UniqueKeyHere with the actual key