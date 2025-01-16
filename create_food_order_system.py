import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime

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

# Check or create user in Firebase
def check_or_create_user(username):
    username = username.lower()  # Ensure usernames are case-insensitive
    user_ref = db.reference(f'/users/shop/{username}')
    user_data = user_ref.get()

    if user_data:
        print(f"Welcome back, {username.capitalize()}!")
    else:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        user_ref.set({'created_at': timestamp})
        print(f"Welcome for the first time, {username.capitalize()}!")

    return username

# Show menu to the user
def show_menu():
    print("\nAvailable Items:")
    for item_id, item in orders_data.items():
        print(f"{item_id}. {item['name']} - ${item['price']}")
    print("")

# Process an order
def process_order(username):
    total_price = 0
    order_ref = db.reference(f'/users/shop/{username}/orders')

    # Create a new parent order ID
    parent_order_id = order_ref.push().key  # Generate a new unique parent order ID
    print(f"Creating a new order session. Order ID: {parent_order_id}")

    order_details_ref = db.reference(f'/users/shop/{username}/orders/{parent_order_id}')
    order_details_ref.set({'order_items': [], 'total_price': 0})  # Initialize the order with empty items and price

    while True:
        show_menu()
        order_id = input("Enter the item number to order (or type 'done' to finish): ").strip()

        if order_id.lower() == 'done':
            break

        if order_id in orders_data:
            item = orders_data[order_id]
            item_ref = order_details_ref.child('order_items').push()  # Add item to the parent order
            item_ref.set(item)  # Save item data under the order

            total_price += item['price']
            print(f"Added {item['name']} to your order. Current total: ${total_price}")
        else:
            print("Invalid item number. Please try again.")

    # Update total price for the parent order
    order_details_ref.update({'total_price': total_price})
    print(f"Order completed! Total price for Order ID {parent_order_id}: ${total_price}")

    # Save order ID, total price, and timestamp under the user's order history
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    db.reference(f'/users/shop/{username}/orders_history').push().set({
        'order_id': parent_order_id,
        'total_price': total_price,
        'order_time': timestamp
    })
    print(f"Order ID {parent_order_id} with total price ${total_price} and timestamp {timestamp} has been saved under your order history.")


# Main Function
if __name__ == "__main__":
    initialize_firebase()

    # Predefined orders data
    orders_data = {
        "1": {"name": "Burger", "price": 5.99},
        "2": {"name": "Pizza", "price": 8.99},
        "3": {"name": "Pasta", "price": 7.49},
        "4": {"name": "Fries", "price": 2.99},
        "5": {"name": "Soda", "price": 1.99}
    }

    print("Welcome to the Order System!")
    username = input("Enter your name: ").strip()

    # Check or create user and start the ordering process
    username = check_or_create_user(username)
    process_order(username)
