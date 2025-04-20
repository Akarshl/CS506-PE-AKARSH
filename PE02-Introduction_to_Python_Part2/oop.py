class User:
    """
    A class to represent a user profile.
    Attributes:
    first_name (str): The user's first name, last_name (str): The user's last name, age (int): The user's age, email (str): The user's email address, location (str): The user's location """
    def __init__(self, first_name, last_name, age, email, location):
        """
        Initializes a new User object with the given details.
        Parameters:
        first_name (str): First name of the user.
        last_name (str): Last name of the user.
        age (int): Age of the user.
        email (str): Email address of the user.
        location (str): Location of the user.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
    def describe_user(self):
        """
        Prints a summary of the user's information.
        """
        print(f"\nUser Profile Summary:")
        print(f"Name     : {self.first_name} {self.last_name}")
        print(f"Age      : {self.age}")
        print(f"Email    : {self.email}")
        print(f"Location : {self.location}")
    def greet_user(self):
        print(f"\nHello, {self.first_name}! Welcome back!")
# Create user instances
user1 = User("Alice", "Johnson", 28, "alice.j@example.com", "New York")
user2 = User("Bob", "Smith", 35, "bob.smith@example.com", "Los Angeles")
# Call methods
user1.describe_user()
user1.greet_user()
user2.describe_user()
user2.greet_user()