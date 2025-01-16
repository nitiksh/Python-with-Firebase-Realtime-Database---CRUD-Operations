import firebase_admin
from firebase_admin import credentials, db

# Initialize Firebase Admin SDK
cred = credentials.Certificate("serviceAccountKey.json")  # Replace with your JSON file path
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://<your-database-name>.firebaseio.com/'
})

# Function to fetch and print all data from the Firebase Realtime Database
def fetch_and_print_all_data():
    # Get all users from the database
    users_ref = db.reference('/users/shop')
    all_users = users_ref.get()
    
    if not all_users:
        print("No users found in the system.")
        return

    print("All Users Data:\n")
    
    # Iterate through each user
    for username, user_data in all_users.items():
        print(f"Username: {username}")
        print(f"Created At: {user_data.get('created_at', 'N/A')}")
        
        # Print the user's orders
        if 'orders' in user_data:
            print("Orders:")
            for order_id, order_data in user_data['orders'].items():
                print(f"  Order ID: {order_id}")
                print(f"    Total Price: {order_data['total_price']}")
                if 'order_items' in order_data:
                    for item_id, item in order_data['order_items'].items():
                        print(f"      Item: {item['name']} - Price: {item['price']}")
                else:
                    print("      No items found in this order.")
        
        # Print the user's order history
        if 'orders_history' in user_data:
            print("Order History:")
            for order_id, history_data in user_data['orders_history'].items():
                print(f"  Order ID: {order_id}")
                print(f"    Order Time: {history_data['order_time']}")
                print(f"    Total Price: {history_data['total_price']}")
        else:
            print("No order history found for this user.")

        print("\n" + "-"*50 + "\n")

# Fetch and print all data
fetch_and_print_all_data()
