from class_base import AppUser

class AdminUser(AppUser):
    """
    AdminUser extends AppUser adding user_role and user_id
    """

    def __init__(self, user_name='unknown', contact='undefined', user_role='Guest', user_id=-1):
        super().__init__(user_name, contact)
        self.user_role = user_role
        self.user_id = user_id
        self.set_last_seen()  # update last_seen

    # Setter & Getter for user_role
    def set_user_role(self, role):
        self.user_role = role
    def get_user_role(self):
        return self.user_role

    # Setter & Getter for user_id
    def set_user_id(self, new_id):
        self.user_id = new_id
    def get_user_id(self):
        return self.user_id

    # Override display_data
    def display_data(self):
        super().display_data()
        print(f'Role: {self.user_role}')
        print(f'User ID: {self.user_id}')
        print(f'Most Recent Access: {self.get_last_seen()}')