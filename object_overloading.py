from AppUser import AppUser
from AdminUser import AdminUser
from FullUser import FullUser, UserRole

def main():
    print('\\nWelcome to Lab 23: Polymorphism and FullUser Overloaded Constructor')

    user_pool = []
    valid_users = []

    while True:
        print("\\nMenu:")
        print("1. Create AppUser")
        print("2. Create AdminUser")
        print("3. Create FullUser from existing object")
        print("4. Create FullUser from direct input")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Preferred Name: ")
            contact = input("Contact Data: ")
            user = AppUser(name, contact)
            user_pool.append(user)
            print("AppUser created:")
            user.display_data()

        elif choice == '2':
            name = input("Preferred Name: ")
            contact = input("Contact Data: ")
            role = input("Role (Guest, Client, Operator, Admin): ")
            uid = int(input("User ID: "))
            admin = AdminUser(name, contact, role, uid)
            user_pool.append(admin)
            print("AdminUser created:")
            admin.display_data()

        elif choice == '3':
            print("Select an existing user object to convert into FullUser:")
            for i, user in enumerate(user_pool):
                print(f"{i}: {user.get_user_name()}")
            idx = int(input("Enter index: "))
            if 0 <= idx < len(user_pool):
                base_user = user_pool.pop(idx)
                full_user = FullUser(base_user)
                valid_users.append(full_user)
                print("FullUser created from object:")
                full_user.display_data()
            else:
                print("Invalid index.")

        elif choice == '4':
            name = input("Preferred Name: ")
            contact = input("Contact Data: ")
            role = input("Role (Guest, Client, Operator, Admin): ")
            uid = int(input("User ID: "))
            full_user = FullUser(name, contact, role, uid)
            valid_users.append(full_user)
            print("FullUser created from direct input:")
            full_user.display_data()

        elif choice == '5':
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()