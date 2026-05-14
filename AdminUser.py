from AppUser import AppUser
from enum import Enum

class UserRole(Enum):
    Admin = 'Admin'
    Operator = 'Operator'
    Guest = 'Guest'

class AdminUser(AppUser):
    def __init__(self, user_name, contact, user_role, user_id):
        super().__init__(user_name, contact)
        self.user_role = UserRole(user_role)
        self.user_id = user_id

    def display_data(self):
        print(f"[AdminUser] Name: {self.user_name} | Contact: {self.contact} | Role: {self.user_role.value} | ID: {self.user_id}")
