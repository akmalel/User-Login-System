from AppUser import AppUser
from AdminUser import AdminUser
from enum import Enum

class UserRole(Enum):
    GUEST = "Guest"
    CLIENT = "Client"
    OPERATOR = "Operator"
    ADMIN = "Admin"

class FullUser(AdminUser):
    """
    FullUser extends AdminUser adding user_directory
    Attributes:
        user_directory (str)
    Methods:
        __init__(self, *args, **kwargs)
    """

    def __init__(self, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], AdminUser):
            admin_user = args[0]
            super().__init__(admin_user.user_name, admin_user.contact,
                             admin_user.user_role, admin_user.user_id)
            self.user_role = UserRole[self.user_role.upper()]
            self.user_directory = f'directory_{admin_user.user_id}'
        elif len(args) == 1 and isinstance(args[0], AppUser):
            app_user = args[0]
            role = kwargs.pop('user_role', 'Guest')
            uid = kwargs.pop('user_id', -2)
            super().__init__(app_user.user_name, app_user.contact, role, uid)
            self.user_role = UserRole[self.user_role.upper()]
            self.user_directory = f'directory_{self.user_id}'
        else:
            self.user_name = args[0] if len(args) > 0 else 'undefined'
            self.contact = args[1] if len(args) > 1 else 'unknown'
            self.user_role = args[2] if len(args) > 2 else 'Guest'
            self.user_id = args[3] if len(args) > 3 else -2
            super().__init__(self.user_name, self.contact, self.user_role, self.user_id)
            self.user_role = UserRole[self.user_role.upper()]
            self.user_directory = f'directory_{self.user_id}'

        self.set_last_seen()  # update access timestamp

    def set_user_directory(self, new_dir):
        self.user_directory = new_dir

    def get_user_directory(self):
        return self.user_directory

    def display_data(self):
        super().display_data()
        print(f'Directory: {self.get_user_directory()}')