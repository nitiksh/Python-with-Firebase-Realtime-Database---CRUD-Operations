import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Realtime Database
def initialize_firebase():
    cred = credentials.Certificate("serviceAccountKey.json")  # Replace with your JSON file path
    firebase_admin.initialize_app(cred, {'databaseURL': 'https://<your-database-name>.firebaseio.com/'})

# Function to delete the /employee node from Firebase if it exists
def delete_employee_node():
    ref = db.reference("/employee")  # Reference to '/employee' node in Firebase
    employee_data = ref.get()  # Get the current data at this reference
    
    if employee_data:  # If the /employee node exists and has data
        ref.delete()  # Delete the entire /employee node
        print("The '/employee' node has been deleted from Firebase.")
    else:
        print("No '/employee' node found to delete in Firebase.")

# Main function
if __name__ == "__main__":
    initialize_firebase()  # Initialize Firebase
    
    # Delete the /employee node if it exists
    delete_employee_node()
