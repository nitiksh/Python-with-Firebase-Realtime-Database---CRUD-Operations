import firebase_admin
from firebase_admin import credentials, db
import csv

# Initialize Firebase Realtime Database
def initialize_firebase():
    try:
        cred = credentials.Certificate("serviceAccountKey.json")  # Replace with your JSON file path
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'https://<your-database-name>.firebaseio.com//'  # Replace with your Firebase Realtime Database URL
        })
        print("Successfully connected to Firebase Realtime Database!")
    except Exception as e:
        print("Error initializing Firebase:", e)
        exit()

# Function to read the CSV file and add data to Firebase
def add_data_to_firebase(csv_file_path):
    try:
        with open(csv_file_path, mode='r') as file:
            # Create a CSV reader object
            csv_reader = csv.DictReader(file)
            
            # Reference to the Firebase database path where student data will be stored
            ref = db.reference('/students')
            
            # Loop through the rows of the CSV file and add them to Firebase
            for row in csv_reader:
                student_name = row['Name'].strip().lower()  # Using lowercase for consistent naming in Firebase
                student_data = {
                    'Name': row['Name'],
                    'Age': int(row['Age']),
                    'Gender': row['Gender'],
                    'Grade': row['Grade'],
                    'School': row['School']
                }
                
                # Push student data to Firebase under the student's name (keyed by name)
                ref.child(student_name).set(student_data)
                print(f"Added data for {row['Name']} to Firebase.")

    except Exception as e:
        print("Error reading CSV or adding data to Firebase:", e)

# Main function to initialize Firebase and add the data from the CSV
def main():
    initialize_firebase()
    csv_file_path = 'students_data.csv'  # Path to your CSV file
    add_data_to_firebase(csv_file_path)

# Run the program
if __name__ == "__main__":
    main()
