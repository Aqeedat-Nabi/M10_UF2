import json

class User:
    def __init__(self, first_name, last_name, age, email, username, password):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.username = username
        self.password = password

    # Getters & Setters
    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_age(self):
        return self.age

    def get_email(self):
        return self.email

    def get_username(self):
        return self.username

    def get_password(self):
        return self.password

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_age(self, age):
        self.age = age

    def set_email(self, email):
        self.email = email

    def set_username(self, username):
        self.username = username

    def set_password(self, password):
        self.password = password


    def display(self):
        print("User Information : ")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Username: {self.username}")
        print(f"Password: {self.password}")

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "age": self.age,
            "email": self.email,
            "username": self.username,
            "password": self.password
        }

# OBJ :
user_obj = User("Alex", "John", 25, "alex.john@gmail.com", "alexjohn", "password1234")
user_obj.display()
print(f"The User Information is as follows : \n {user_obj.to_dict()}")
