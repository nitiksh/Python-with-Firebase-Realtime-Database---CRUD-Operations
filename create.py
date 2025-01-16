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

# Create data using different methods
def create_data():
    try:
        # String data
        db.reference('/example/string').set("Hello, Firebase!")
        print("String data saved!")

        # Integer data
        db.reference('/example/integer').set(42)
        print("Integer data saved!")

        # Float data
        db.reference('/example/float').set(3.14159)
        print("Float data saved!")

        # Boolean data
        db.reference('/example/boolean').set(True)
        print("Boolean data saved!")

        # Dictionary (Object) data
        user_data = {
            "name": "Alice",
            "email": "alice@example.com",
            "age": 25
        }
        db.reference('/example/dictionary').set(user_data)
        print("Dictionary data saved!")

        # List (Array) data
        hobbies = ["reading", "traveling", "coding"]
        db.reference('/example/list').set(hobbies)
        print("List data saved!")

        # Push method (Auto-generated keys)
        db.reference('/example/push').push({"item": "Auto-generated key example"})
        print("Data with auto-generated key saved!")

    except Exception as e:
        print("Error saving data:", e)

# Main Function
if __name__ == "__main__":
    initialize_firebase()
    create_data()