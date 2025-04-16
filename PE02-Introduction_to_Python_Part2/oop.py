class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location
    def describe_user(self):
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