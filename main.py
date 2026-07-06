from cryptography.fernet import Fernet
import os


def create_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as file:
            file.write(key)


def load_key():
    with open("key.key", "rb") as file:
        return file.read()


def add_password():
    website = input("Website: ")
    username = input("Username: ")
    password = input("Password: ")

    key = load_key()
    cipher = Fernet(key)

    encrypted = cipher.encrypt(password.encode())

    with open("passwords.txt", "ab") as file:
        file.write(
            website.encode()
            + b"|"
            + username.encode()
            + b"|"
            + encrypted
            + b"\n"
        )

    print("Password saved 🔐")


def view_passwords():
    key = load_key()
    cipher = Fernet(key)

    with open("passwords.txt", "rb") as file:
        for line in file:
            data = line.strip().split(b"|")

            print(
                "Website:",
                data[0].decode(),
                "Username:",
                data[1].decode(),
                "Password:",
                cipher.decrypt(data[2]).decode()
            )


create_key()


while True:
    print("""
1. Add Password
2. View Passwords
3. Exit
""")

    choice = input("Choose: ")

    if choice == "1":
        add_password()

    elif choice == "2":
        view_passwords()

    elif choice == "3":
        break