import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Realtime Database
try:
    # Provide the path to your Firebase Admin SDK private key JSON file
    cred = credentials.Certificate("serviceAccountKey.json")  # Replace with the path to your JSON file
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://<your-database-name>.firebaseio.com/'
    })
    
    print("Successfully connected to Firebase Realtime Database!")
except Exception as e:
    print("Error connecting to Firebase Realtime Database:", e)