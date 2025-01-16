import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Realtime Database
def initialize_firebase():
    cred = credentials.Certificate("serviceAccountKey.json")  # Replace with your JSON file path
    firebase_admin.initialize_app(cred, {'databaseURL': 'https://<your-database-name>.firebaseio.com/'})

# Function to create tourist data
def create_tourist_data():
    tourists = {
        "Alice": {"country": "USA", "age": 30, "destination": "Paris"},
        "Bob": {"country": "Canada", "age": 25, "destination": "Tokyo"},
        "Charlie": {"country": "UK", "age": 35, "destination": "New York"}
    }
    ref = db.reference("/tourists")  # Reference to tourists node in Firebase
    ref.set(tourists)  # Push the tourist data into Firebase

# Function to read tourist data
def read_tourist_data():
    ref = db.reference("/tourists")  # Reference to tourists node in Firebase
    tourists_data = ref.get()  # Fetch the data from Firebase
    print("Tourist Data:")
    for name, info in tourists_data.items():
        print(f"Name: {name}, Country: {info['country']}, Age: {info['age']}, Destination: {info['destination']}")

# Main function
if __name__ == "__main__":
    initialize_firebase()  # Initialize Firebase
    create_tourist_data()   # Create tourist data
    read_tourist_data()     # Read and display tourist data