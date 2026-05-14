class AppUser:
    def __init__(self, user_name, contact):
        self.user_name = user_name
        self.contact = contact

    def display_data(self):
        print(f"[AppUser] Name: {self.user_name} | Contact: {self.contact}")
