import pickle
import sqlite3
import json
from AppUser import AppUser
from AdminUser import AdminUser
from FullUser import FullUser, UserRole

def save_pickle(user_pool):
    with open('users.pkl', 'wb') as f:
        pickle.dump(user_pool, f)
    print("Users saved to 'users.pkl' (Pickle).")

def load_pickle():
    with open('users.pkl', 'rb') as f:
        users = pickle.load(f)
    print("Users loaded from 'users.pkl':")
    for u in users:
        u.display_data()
    return users

def save_json(user_pool):
    metadata = []
    for user in user_pool:
        metadata.append({
            'user_name': user.user_name,
            'contact': user.contact,
            'type': type(user).__name__,
            'user_role': getattr(user, 'user_role', None).value if getattr(user, 'user_role', None) else None,
            'user_id': getattr(user, 'user_id', None)
        })
    with open('users.json', 'w') as f:
        json.dump(metadata, f, indent=4)
    print("Users saved to 'users.json' (JSON).")

def save_sql(user_pool):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            user_name TEXT,
            contact TEXT,
            user_role TEXT,
            user_id INTEGER,
            data BLOB
        )
    ''')
    for i, user in enumerate(user_pool):
        data_blob = pickle.dumps(user)
        role = getattr(user, 'user_role', None)
        if role is not None:
            role = role.value
        uid = getattr(user, 'user_id', None)
        c.execute('INSERT INTO users (id, user_name, contact, user_role, user_id, data) VALUES (?, ?, ?, ?, ?, ?)',
                  (i, user.user_name, user.contact, role, uid, data_blob))
    conn.commit()
    print("Users saved to SQLite database 'users.db'.")
    conn.close()

def main():
    print('\\nWelcome to Lab 24: Persistent User Login System')

    # Example objects
    user_pool = [
        AppUser('Alice', 'alice@example.com'),
        AdminUser('Bob', 'bob@example.com', 'Admin', 101),
        FullUser('Charlie', 'charlie@example.com', 'Operator', 202)
    ]

    while True:
        print("\\nMenu:")
        print("1. Display all users")
        print("2. Save users using Pickle")
        print("3. Save users using JSON")
        print("4. Save users to SQLite")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            for user in user_pool:
                user.display_data()
        elif choice == '2':
            save_pickle(user_pool)
        elif choice == '3':
            save_json(user_pool)
        elif choice == '4':
            save_sql(user_pool)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
