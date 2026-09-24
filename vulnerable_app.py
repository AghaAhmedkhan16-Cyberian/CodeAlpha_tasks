# Intentionally vulnerable code for secure-coding review
USERNAME = "admin"
PASSWORD = "admin123"  # Hardcoded credential

def login():
    username = input("Username: ")
    password = input("Password: ")

    if username == USERNAME and password == PASSWORD:
        print("Login successful! Welcome " + username)
    else:
        print("Login failed: invalid username or password for account " + username)

login()
