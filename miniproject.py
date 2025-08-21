import json

# -----------------------------
# Node and LinkedList Classes
# -----------------------------
class Node:
    def __init__(self, data, next=None):
        self.data = data  # data will be a dictionary
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        """Insert new user data at the end of the linked list."""
        if self.head is None:
            self.head = Node(data)
            return
        i = self.head
        while i.next:
            i = i.next
        i.next = Node(data)

    def print_list(self):
        """Print all user data stored in the linked list."""
        if self.head is None:
            print("No users found in Linked List.")
            return
        i = self.head
        while i:
            print(i.data)
            i = i.next


# -----------------------------
# File Handling Functions
# -----------------------------
FILEPATH = "D:\\aienginner\\month 1\\week3\\data.txt"

def save_to_file(data):
    """Append new user data (dict) to file."""
    try:
        with open(FILEPATH, "a") as f:
            f.write(json.dumps(data) + "\n")  # store as JSON string
    except Exception as e:
        print("Error saving to file:", e)

def load_from_file():
    """Load all users from file into a list of dicts."""
    users = []
    try:
        with open(FILEPATH, "r") as f:
            for line in f:
                users.append(json.loads(line.strip()))
    except FileNotFoundError:
        pass  # file not created yet
    return users


# -----------------------------
# Functionalities
# -----------------------------
def admin_panel(linked_list):
    username = input("Enter admin username: ").lower()
    password = input("Enter admin password: ").lower()

    if username == "haider" and password == "miniproject":
        print("\n--- Admin Access Granted ---")
        print("All registered users:")
        linked_list.print_list()
    else:
        print("Invalid Admin credentials!")


def create_account(linked_list):
    print("\n--- Create New Account ---")
    name = input("Enter name: ")
    age = input("Enter age: ")
    gender = input("Enter gender: ")
    password = input("Set password: ")

    user = {
        "name": name,
        "age": age,
        "gender": gender,
        "password": password
    }

    # Insert into linked list
    linked_list.insert_at_end(user)
    # Save to file
    save_to_file(user)
    print("Account created successfully!\n")


def user_login():
    print("\n--- User Login ---")
    username = input("Enter your name: ")
    password = input("Enter your password: ")

    users = load_from_file()
    for u in users:
        if u["name"] == username and u["password"] == password:
            print(f"Welcome {username}, Login Successful!\n")
            return
    print("Invalid username or password.\n")


# -----------------------------
# Main Program Loop
# -----------------------------
if __name__ == "__main__":
    linked_list = LinkedList()

    # Load existing data into linked list on startup
    existing_users = load_from_file()
    for u in existing_users:
        linked_list.insert_at_end(u)

    while True:
        print("\n===== MENU =====")
        print("1. Admin Login")
        print("2. Create Account")
        print("3. User Login")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            admin_panel(linked_list)
        elif choice == "2":
            create_account(linked_list)
        elif choice == "3":
            user_login()
        elif choice == "4":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice, try again.")
